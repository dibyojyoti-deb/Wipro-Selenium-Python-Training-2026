import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import SwitchLocators

class SwitchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def take_screenshot(self, name):
        self.driver.save_screenshot(f"{name}.png")

    def handle_iframe(self, text_to_send):
        # 1. Wait for iframe and switch
        print("Action: Switching to Iframe...")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(SwitchLocators.IFRAME_ID))
        
        # 2. Locate the body inside the iframe
        input_field = self.wait.until(EC.presence_of_element_located(SwitchLocators.IFRAME_BODY))
        
        # 3. Use JavaScript to clear (Solves InvalidElementStateException)
        self.driver.execute_script("arguments[0].innerHTML = '';", input_field)
        
        # 4. Enter new text
        input_field.send_keys(text_to_send)
        self.take_screenshot("Screenshot1_InsideIframe")
        
        # 5. Switch back to main content
        self.driver.switch_to.default_content()
        print("Action: Returned to Main Content.")

    def handle_windows(self):
        # ... (Rest of the handle_windows code remains the same)
        parent_handle = self.driver.current_window_handle
        self.wait.until(EC.element_to_be_clickable(SwitchLocators.NEW_WINDOW_BUTTON)).click()
        self.wait.until(lambda d: len(d.window_handles) > 1)
        
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)
            print(f"Window Handle: {handle} | Title: {self.driver.title}")
            if handle != parent_handle:
                self.take_screenshot("Screenshot2_ChildWindow")
                self.driver.close()
        
        self.driver.switch_to.window(parent_handle)
        self.take_screenshot("Screenshot3_FinalParent")