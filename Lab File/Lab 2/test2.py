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
        self.log = open("ninja_execution_log.txt", "w", encoding="utf-8")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass

sys.stdout = Logger()

class TestTc002():
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
    
    def teardown_method(self):
        self.driver.quit()
        if hasattr(sys.stdout, 'log'):
            sys.stdout.log.close()
    
    def test_tc002(self):
        try:
            print(f"Execution Started: {time.ctime()}")
            self.driver.get("https://tutorialsninja.com/demo/index.php?route=product/product&product_id=42")
            
            # 1. Fill Quantity
            qty = self.wait.until(EC.presence_of_element_located((By.ID, "input-quantity")))
            qty.clear()
            qty.send_keys("2")
            print("Action: Filled quantity.")

            # 2. Fill all Text/Textarea fields (Just in case they are mandatory)
            text_fields = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']:not(#input-quantity), textarea")
            for field in text_fields:
                if field.is_displayed():
                    field.send_keys("Testing Input")
            print("Action: Filled all visible text/textarea fields.")

            # 3. Select Radio Button
            radios = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='radio']")))
            self.driver.execute_script("arguments[0].click();", radios[0])
            print("Action: Clicked Radio Button.")

            # 4. Select Checkbox
            checkboxes = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox']")))
            self.driver.execute_script("arguments[0].click();", checkboxes[0])
            print("Action: Clicked Checkbox.")

            # 5. Select Dropdown
            dropdowns = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "select")))
            for d in dropdowns:
                select = Select(d)
                select.select_by_index(1) 
            print("Action: Handled all dropdowns.")
            
            self.driver.save_screenshot("Screenshot2_FormFilled.png")

            # 6. Click Add to Cart
            submit_btn = self.driver.find_element(By.ID, "button-cart")
            self.driver.execute_script("arguments[0].click();", submit_btn)
            print("Action: Clicked Add to Cart.")

            # 7. Final Verification (Look for the Success Banner using Presence instead of Visibility)
            # Sometimes the banner is in the DOM but 'hidden' by CSS transitions initially
            success_xpath = "//div[contains(@class, 'alert-success')] | //div[contains(., 'Success') and contains(@class, 'alert')]"
            success_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, success_xpath)))
            
            print(f"Verification: Found success notification.")
            
            self.driver.save_screenshot("Screenshot3_FinalVerification.png")
            print("Result: Test Passed Successfully.")

        except Exception as e:
            print(f"Result: Test Failed. Error: {type(e).__name__}")
            # Check the screenshot—if you see RED text on the page, a mandatory field was missed
            self.driver.save_screenshot("Error_Screenshot.png")

if __name__ == "__main__":
    test = TestTc002()
    test.setup_method()
    try:
        test.test_tc002()
    finally:
        test.teardown_method()