import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- LOGGING SETUP ---
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("alert_execution_log.txt", "w", encoding="utf-8")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass

sys.stdout = Logger()

# --- SELENIUM SCRIPT ---
driver = webdriver.Chrome()

try:
    print(f"Execution Started: {time.ctime()}")
    driver.get("https://letcode.in/alert")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # 1. Triggers and Accepts a Simple Alert
    driver.find_element(By.ID, "accept").click()
    alert = wait.until(EC.alert_is_present())
    print(f"Simple Alert Message: {alert.text}")
    alert.accept() 
    driver.save_screenshot("Screenshot1_SimpleAlert.png")

    # 2. Dismisses a Confirmation Pop-up
    driver.find_element(By.ID, "confirm").click()
    confirm_alert = wait.until(EC.alert_is_present())
    print(f"Confirm Alert Message: {confirm_alert.text}")
    confirm_alert.dismiss() 
    driver.save_screenshot("Screenshot2_ConfirmDismissed.png")

    # 3. Enters text in a Prompt Alert and Accepts it
    driver.find_element(By.ID, "prompt").click()
    prompt_alert = wait.until(EC.alert_is_present())
    
    # Updated Name to DJ
    user_name = "DJ" 
    prompt_alert.send_keys(user_name)
    prompt_alert.accept()
    print(f"Prompt accepted with text: {user_name}")

    # 4. Verifies the result displayed on the page
    result_element = driver.find_element(By.ID, "myName")
    result_text = result_element.text
    print(f"Verification Message on Page: {result_text}")
    
    # Ensure the name 'DJ' is actually present in the result text
    assert user_name in result_text
    driver.save_screenshot("Screenshot3_FinalResult.png")
    
    print("Execution Completed Successfully - Verified name 'DJ' on page.")

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("Error_Screenshot.png")

finally:
    time.sleep(2)
    driver.quit()
    sys.stdout.log.close()