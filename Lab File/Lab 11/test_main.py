import sys
import unittest
import time
from selenium import webdriver
from pages import OpencartPage

# --- TERMINAL LOGGING SETUP ---
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Lab_POM_Output.txt", "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger()

class TestLabPOM(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://tutorialsninja.com/demo/")
        self.page = OpencartPage(self.driver)

    def test_opencart_flow(self):
        print(f"--- Execution Started: {time.ctime()} ---")
        
        # Screenshot 1: Homepage
        self.page.take_screenshot("Screenshot1_Home")
        print("Step 1: Navigating to Mac section...")
        self.page.navigate_to_mac_section()
        
        # Screenshot 2: Mac Category
        self.page.take_screenshot("Screenshot2_MacPage")
        print("Step 2: Verifying Heading and Sorting...")
        assert self.page.get_mac_heading_text() == "Mac"
        self.page.sort_products("Name (A - Z)")
        
        print("Step 3: Adding product to cart...")
        self.page.click_add_to_cart()
        
        # Screenshot 3: Search Results
        print("Step 4: Performing search for 'Monitors'...")
        self.page.search_for_product("Monitors")
        self.page.take_screenshot("Screenshot3_SearchMonitors")
        
        print("Step 5: Executing refined search with descriptions...")
        self.page.refined_search()
        
        # Screenshot 4: Final State
        self.page.take_screenshot("Screenshot4_FinalState")
        print("Result: Test Passed successfully. All evidence captured.")

    def tearDown(self):
        print(f"--- Execution Finished: {time.ctime()} ---")
        self.driver.quit()
        # Close the log file handle
        if hasattr(sys.stdout, 'log'):
            sys.stdout.log.close()

if __name__ == "__main__":
    unittest.main()