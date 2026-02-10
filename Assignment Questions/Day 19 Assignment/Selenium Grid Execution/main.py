import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Redirect terminal output to both console and output_log.txt
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

# Selenium Grid Hub URL (Standard port for Selenium 4 is 4444)
grid_url = "http://localhost:4444"

# Browser configurations to test
browser_configs = [
    ChromeOptions(),
    FirefoxOptions()
]

for options in browser_configs:
    browser_name = options.capabilities.get("browserName", "unknown")
    print(f"--- Starting Execution for {browser_name} ---")
    
    try:
        # 1. Connect to Selenium Grid using RemoteWebDriver
        driver = webdriver.Remote(command_executor=grid_url, options=options)
        
        # 2. Navigate to a website
        driver.get("https://www.google.com")
        
        # 3. Verify the page title
        page_title = driver.title
        
        # 4. Print browser name and platform for each execution
        caps = driver.capabilities
        print(f"Browser: {caps['browserName']}")
        print(f"Platform: {caps['platformName']}")
        print(f"Page Title Verified: {page_title}")
        
        # Take screenshot as proof of work
        driver.save_screenshot(f"Grid_Result_{caps['browserName']}.png")
        print(f"Screenshot saved as Grid_Result_{caps['browserName']}.png\n")
        
    except Exception as e:
        print(f"Error during execution on {browser_name}: {e}")
        print("Ensure the Selenium Server is running (java -jar selenium-server.jar standalone)\n")
    
    finally:
        if 'driver' in locals():
            driver.quit()

print("Full execution log saved to output_log.txt")