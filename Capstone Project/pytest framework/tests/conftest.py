import pytest
import os
import sys
import glob
import time
import configparser
import argparse
import undetected_chromedriver as uc
import psutil
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions

# Prevent undetected chromedriver destructor crash
def suppress_del(self):
    pass

uc.Chrome.__del__ = suppress_del

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from utilities.data_loader import load_kv_csv

DATA_DIR = os.path.join(BASE_DIR, "data")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

# ---------------- CONFIG READER ---------------- #

CONFIG_PATH = os.path.join(BASE_DIR, "config", "config.ini")
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# ---------------- CLI OPTIONS ---------------- #

def pytest_addoption(parser):
    try:
        parser.addoption(
            "--browser",
            action="store",
            default=None,
            choices=["chrome", "edge"],
            help="Browser to use: chrome or edge (overrides config.ini)"
        )
    except argparse.ArgumentError:
        pass

# ---------------- TERMINAL LOG FILE ---------------- #

def pytest_configure(config):
    log_file = os.path.join(REPORT_DIR, "pytest_terminal_output.txt")
    with open(log_file, "w") as f:
        f.write(f"PYTEST EXECUTION LOG\nStarted: {time.ctime()}\n====================\n")

# ---------------- DYNAMIC CSV PARAMETRIZATION ---------------- #

def pytest_generate_tests(metafunc):
    if "setup" in metafunc.fixturenames:
        csv_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.csv")))
        # This creates 2 iterations of your 25 tests = 50 tests total
        metafunc.parametrize("setup", csv_files, indirect=True)

# ---------------- FORCE BROWSER TERMINATION ---------------- #

def kill_browser_process(driver):
    try:
        if driver and driver.service and driver.service.process:
            pid = driver.service.process.pid
            driver.quit()
            if psutil.pid_exists(pid):
                proc = psutil.Process(pid)
                for child in proc.children(recursive=True):
                    child.terminate()
                proc.terminate()
    except:
        pass

# ---------------- MAIN FIXTURE ---------------- #

@pytest.fixture(scope="class")
def setup(request):
    csv_path = request.param
    test_data = load_kv_csv(csv_path)

    # Outsmart the plugin's default value. 
    if "--browser" in sys.argv or any(arg.startswith("--browser=") for arg in sys.argv):
        browser = request.config.getoption("--browser").lower()
    else:
        browser = config.get("DEFAULT", "browser", fallback="chrome").lower()

    driver = None

    if browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-popup-blocking")
        
        # --- EDGE STEALTH MODE START ---
        edge_options.add_argument("--disable-blink-features=AutomationControlled")
        edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        edge_options.add_experimental_option("useAutomationExtension", False)
        # --- EDGE STEALTH MODE END ---

        try:
            driver = webdriver.Edge(options=edge_options)
            
            # Execute CDP command to hide the webdriver flag from Cloudflare
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            })
        except Exception:
            pytest.fail("FATAL: Could not initialize Edge driver.")
            
    else:
        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-blink-features=AutomationControlled") # CAPTCHA stealth

        for _ in range(3):
            try:
                driver = uc.Chrome(options=options) 
                break
            except Exception:
                time.sleep(2)

        if not driver:
            pytest.fail("FATAL: Could not initialize Chrome driver.")

    implicit_wait = config.getint("DEFAULT", "implicit_wait", fallback=5)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(implicit_wait)

    request.cls.driver = driver
    request.cls.data = test_data

    base_url = config.get("DEFAULT", "base_url", fallback=test_data.get("base_url"))

    try:
        driver.get(base_url)
        # Wait out initial Cloudflare check if present
        time.sleep(3) 
    except Exception:
        pass

    yield

    kill_browser_process(driver)

# ---------------- LOG PASS/FAIL TO FILE ---------------- #

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.when == "call":
        log_path = os.path.join(REPORT_DIR, "pytest_terminal_output.txt")
        status = "PASS" if report.passed else "FAIL"
        try:
            with open(log_path, "a") as f:
                f.write(f"{status}: {report.nodeid}\n")
        except:
            pass