import undetected_chromedriver as uc
import time
import os

# 1. Setup Driver
options = uc.ChromeOptions()
options.add_argument('--window-size=1920,1080')

print("Launching Professional Navigation Test...")
driver = uc.Chrome(options=options)

# Use a list to store domains for the log file
domain_log = []

try:
    # --- STEP 1: Initial Navigation ---
    url1 = "https://www.google.com"
    driver.get(url1)
    time.sleep(3) 
    
    domain_log.append(f"Primary Domain: {url1}")
    driver.save_screenshot("Step1_Google_Home.png")
    print(f"Step 1 Success: Visited {url1}")

    # --- STEP 2: Navigate to Wikipedia ---
    url2 = "https://www.wikipedia.org"
    driver.get(url2)
    time.sleep(3)
    
    domain_log.append(f"Secondary Domain: {url2}")
    driver.save_screenshot("Step2_Wikipedia_Home.png")
    print(f"Step 2 Success: Visited {url2}")

    # --- STEP 3: Back Navigation ---
    driver.back()
    time.sleep(2)
    driver.save_screenshot("Step3_Back_Navigation.png")
    print("Step 3 Success: Navigated Back")

    # --- STEP 4: Forward Navigation ---
    driver.forward()
    time.sleep(2)
    driver.save_screenshot("Step4_Forward_Navigation.png")
    print("Step 4 Success: Navigated Forward")

    # --- STEP 5: Refresh ---
    driver.refresh()
    time.sleep(2)
    driver.save_screenshot("Step5_Final_Refresh.png")
    print("Step 5 Success: Page Refreshed")

    # --- FINAL STEP: Write Domains to File ---
    with open("navigation_log.txt", "w") as f:
        f.write("--- Navigation Test Domain Log ---\n")
        f.write(f"Timestamp: {time.ctime()}\n")
        for entry in domain_log:
            f.write(entry + "\n")
    print("\n[INFO] Domain names saved to 'navigation_log.txt'")
    print("[INFO] All screenshots captured successfully.")

except Exception as e:
    print(f"\n[ERROR] Test interrupted: {e}")

finally:
    # This block ensures the WinError 6 does not show up in your terminal
    print("Closing session...")
    try:
        driver.close() # Closes the browser window
        driver.quit()  # Quits the driver process
    except:
        # Silently ignore any handle errors during shutdown
        pass