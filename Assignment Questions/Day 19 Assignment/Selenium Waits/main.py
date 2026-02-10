import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Redirect prints to both terminal and a text file
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("output_log.txt", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger()

driver = webdriver.Chrome()
driver.implicitly_wait(5)

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.save_screenshot("Screenshot1_Initial.png")
    
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # Explicit Wait
    wait = WebDriverWait(driver, 10)
    finish_element = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    driver.save_screenshot("Screenshot2_AfterWait.png")

    # Fluent Wait
    fluent_wait = WebDriverWait(driver, 15, poll_frequency=1, 
                                ignored_exceptions=[NoSuchElementException])
    header = fluent_wait.until(EC.presence_of_element_located((By.TAG_NAME, "h4")))

    # Output text and log completion
    print("Element is available for interaction.")
    print(f"Text found: {finish_element.text}")
    driver.save_screenshot("Screenshot3_Final.png")

finally:
    driver.quit()