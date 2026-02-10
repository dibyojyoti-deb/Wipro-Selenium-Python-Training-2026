import unittest
import sys
import time
from selenium import webdriver
from pages import LoginPage, InventoryPage

# --- LOGGING UTILITY ---
class FrameworkLogger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Framework_Output.txt", "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

# Redirecting stdout to our logger
sys.stdout = FrameworkLogger()

class TestSauceDemo(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.saucedemo.com/")
        
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)

    def test_complete_flow(self):
        print(f"--- Framework Execution Started: {time.ctime()} ---")
        
        print("Action: Performing Login...")
        self.login_page.login("standard_user", "secret_sauce")
        
        print("Action: Verifying Dashboard Header...")
        header_text = self.inventory_page.get_header()
        
        self.assertEqual(header_text, "Products")
        print(f"Verification Success: Found header '{header_text}'")
        
        print("Result: Test Status - PASS")

    def tearDown(self):
        print(f"--- Execution Finished: {time.ctime()} ---")
        self.driver.quit()
        if hasattr(sys.stdout, 'log'):
            sys.stdout.log.close()

if __name__ == "__main__":
    unittest.main()