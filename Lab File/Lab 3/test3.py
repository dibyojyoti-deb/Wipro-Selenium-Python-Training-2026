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
        self.log = open("lab_demo_3_log.txt", "w", encoding="utf-8")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass

sys.stdout = Logger()

class TestTc003():
    def setup_method(self):
        # Initializing Firefox as per Lab requirements
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
    
    def teardown_method(self):
        self.driver.quit()
        if hasattr(sys.stdout, 'log'):
            sys.stdout.log.close()
    
    def test_tc003(self):
        try:
            print(f"Execution Started: {time.ctime()}")
            
            # 1. Open URL
            self.driver.get("https://tutorialsninja.com/demo/")
            self.driver.save_screenshot("Screenshot1_Home.png")
            print("Action: Opened TutorialsNinja Home Page.")

            # 2. Go to 'Desktops' tab
            desktops_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Desktops")))
            desktops_link.click()
            print("Action: Clicked on Desktops tab.")

            # 3. Click on 'Mac'
            mac_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Mac (1)")))
            mac_link.click()
            print("Action: Navigated to Mac category.")

            # 4. Select 'Name (A-Z)' from Sort By dropdown
            sort_dropdown = self.wait.until(EC.presence_of_element_located((By.ID, "input-sort")))
            select = Select(sort_dropdown)
            select.select_by_visible_text("Name (A - Z)")
            print("Action: Sorted products by Name (A-Z).")
            self.driver.save_screenshot("Screenshot2_SortedResults.png")

            # 5. Click on 'Add to Cart' button 
            # (Note: On the Mac page, we click the button for the iMac)
            add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add to Cart')]")))
            add_to_cart_btn.click()
            print("Action: Clicked Add to Cart.")

            # 6. Final Verification (Confirmation Message)
            success_banner = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
            )
            print(f"Verification: {success_banner.text.split('×')[0].strip()}")
            
            assert "Success" in success_banner.text
            self.driver.save_screenshot("Screenshot3_FinalSuccess.png")
            print("Result: Lab Demo 3 Completed Successfully.")

        except Exception as e:
            print(f"Result: Test Failed. Error: {type(e).__name__}")
            self.driver.save_screenshot("Error_Lab3.png")

if __name__ == "__main__":
    test = TestTc003()
    test.setup_method()
    try:
        test.test_tc003()
    finally:
        test.teardown_method()