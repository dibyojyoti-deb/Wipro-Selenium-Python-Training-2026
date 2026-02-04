import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 1. Setup Driver
options = uc.ChromeOptions()
options.add_argument('--window-size=1920,1080')

print("Launching Stealth Browser...")
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 25)

try:
    # 2. Go to the registration page
    url = "https://demo.opencart.com/index.php?route=account/register&language=en-gb"
    driver.get(url)
    
    print("Waiting for security check...")
    time.sleep(8) 

    # 3. Fill the Form
    print("Entering data...")
    # Using a unique email based on timestamp so it doesn't fail on 'Email already exists'
    unique_email = f"test_user_{int(time.time())}@example.com"

    wait.until(EC.element_to_be_clickable((By.ID, "input-firstname"))).send_keys("Dibyojyoti")
    driver.find_element(By.ID, "input-lastname").send_keys("Deb")
    driver.find_element(By.ID, "input-email").send_keys(unique_email)
    
    password_field = driver.find_element(By.ID, "input-password")
    driver.execute_script("arguments[0].scrollIntoView();", password_field)
    password_field.send_keys("Testing123!")

    # 4. Privacy Policy & Submit
    agree_check = driver.find_element(By.NAME, "agree")
    driver.execute_script("arguments[0].click();", agree_check)

    print("Submitting Form...")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    driver.execute_script("arguments[0].click();", submit_button)
    
    # 5. VALIDATION & SCREENSHOT
    # Wait for the page to transition
    time.sleep(5) 
    
    # Generate a filename with a timestamp
    screenshot_name = f"Proof_of_Work_{int(time.time())}.png"
    driver.save_screenshot(screenshot_name)
    
    print("-" * 30)
    print(f"SUCCESS: Screenshot saved as '{screenshot_name}'")
    print(f"Used Email: {unique_email}")
    print("-" * 30)

except Exception as e:
    print(f"FAILED: {e}")
    driver.save_screenshot("failure_report.png")

finally:
    # 6. CLEAN EXIT (Fixes the WinError 6)
    print("Cleaning up driver handles...")
    try:
        driver.close() # Close the window first
        driver.quit()  # Then quit the service
    except:
        # If Python 3.13 still complains, we ignore it silently
        pass