import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- LOGGING SETUP ---
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("lab_demo_3_report.txt", "w", encoding="utf-8")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass

sys.stdout = Logger()

class TestOpencartSuite():
    def setup_method(self):
        # Initializing Chrome (Updated as per your request)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
    
    def teardown_method(self):
        self.driver.quit()
        if hasattr(sys.stdout, 'log'):
            sys.stdout.log.close()
    
    def test_opencart_flow_1(self):
        """First Test Case: Full Flow with 'Monitors' Search"""
        try:
            print(f"--- Starting Test Case 1: {time.ctime()} ---")
            
            # Step 1 & 3: Open URL and Verify Title
            self.driver.get("https://tutorialsninja.com/demo/") 
            assert "Your Store" in self.driver.title
            print("Action: Page Title Verified.")

            # Step 4 & 5: Go to Desktops -> Mac
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Desktops"))).click()
            self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Mac (1)"))).click()
            
            # Step 13 & 18: Verify the 'Mac' heading (Added after Step 5)
            mac_heading = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Mac']")))
            assert mac_heading.is_displayed()
            print("Action: 'Mac' Heading Verified.")

            # Step 6: Select 'Name (A-Z)' from Sort By dropdown
            sort_dropdown = Select(self.wait.until(EC.presence_of_element_located((By.ID, "input-sort"))))
            sort_dropdown.select_by_visible_text("Name (A - Z)")
            print("Action: Sorted by Name (A-Z).")

            # Step 7: Click on 'Add to Cart' button
            add_cart = self.driver.find_element(By.XPATH, "//button[contains(.,'Add to Cart')]")
            add_cart.click()
            print("Action: Clicked Add to Cart.")

            # Step 8 & 14: Enter 'Monitors' in 'Search' (Changed from Mobile)
            search_box = self.driver.find_element(By.NAME, "search")
            search_box.clear()
            search_box.send_keys("Monitors")
            self.driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
            print("Action: Searched for 'Monitors'.")

            # Step 9 & 10: Wait and Clear text from 'Search Criteria'
            search_criteria = self.wait.until(EC.presence_of_element_located((By.ID, "input-search")))
            search_criteria.clear()
            print("Action: Cleared Search Criteria text box.")

            # Step 11: Click 'Search in product descriptions' and click Search
            self.driver.find_element(By.ID, "description").click()
            self.driver.find_element(By.ID, "button-search").click()
            print("Action: Final Search with Description enabled.")

            self.driver.save_screenshot("Lab3_Chrome_Final.png")
            print("Result: Test Status PASS")

        except Exception as e:
            print(f"Result: Test Status FAIL. Error: {e}")
            self.driver.save_screenshot("Lab3_Chrome_Error.png")

    def test_opencart_flow_2(self):
        """Step 22: Second Test Case (Suite implementation)"""
        print("\n--- Starting Test Case 2 (Repeat Flow) ---")
        self.test_opencart_flow_1()

# --- Execution Block ---
if __name__ == "__main__":
    suite = TestOpencartSuite()
    suite.setup_method()
    try:
        suite.test_opencart_flow_1() # Run Test Case 1
        suite.test_opencart_flow_2() # Run Test Case 2 (Step 22/23: Suite)
    finally:
        suite.teardown_method()