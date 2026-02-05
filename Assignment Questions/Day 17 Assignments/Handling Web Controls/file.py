import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- LOGGING SETUP ---
# This redirects all print statements to both the console and a text file
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("execution_log.txt", "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger()

# --- SELENIUM SCRIPT ---
driver = webdriver.Chrome()

try:
    print("Execution Started: " + time.ctime())
    driver.get("https://letcode.in/window")
    driver.maximize_window()
    
    # Take Screenshot 1: Initial Page Load
    driver.save_screenshot("Screenshot1.png")
    print("Screenshot1 saved: Initial Page Load.")

    wait = WebDriverWait(driver, 10)
    parent_window = driver.current_window_handle
    print(f"Parent Window ID: {parent_window}")

    # Click the button that opens a new window
    home_btn = wait.until(EC.element_to_be_clickable((By.ID, "home")))
    home_btn.click()

    # Wait for the new window
    wait.until(EC.number_of_windows_to_be(2))
    all_windows = driver.window_handles
    
    # Switch to new window
    for window in all_windows:
        if window != parent_window:
            driver.switch_to.window(window)
            break

    # Take Screenshot 2: Switched to New Window
    print(f"Switched to New Window. Title: {driver.title}")
    driver.save_screenshot("Screenshot2.png")
    print("Screenshot2 saved: New Window view.")

    # Close and return
    driver.close() 
    driver.switch_to.window(parent_window)
    print("Returned to Parent Window.")

    # Final Action: Click Multi-window button
    multi_btn = driver.find_element(By.ID, "multi")
    multi_btn.click()
    time.sleep(2) 

    # Take Screenshot 3: Final State
    driver.save_screenshot("Screenshot3.png")
    print("Screenshot3 saved: Multi-window state.")
    print("Execution Completed Successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("Error_Screenshot.png")

finally:
    driver.quit()
    # Close the log file handle
    sys.stdout.log.close()