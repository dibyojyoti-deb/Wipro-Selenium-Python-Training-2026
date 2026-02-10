import sys
import unittest
import time
from selenium import webdriver
from pages import SwitchPage

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("Switching_Lab_Output.txt", "w", encoding="utf-8")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self): pass

sys.stdout = Logger()

class TestSwitchingFlow(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.page = SwitchPage(self.driver)

    def test_context_switching(self):
        print(f"--- Switch Test Started: {time.ctime()} ---")
        
        # Task 1 & 2: Iframes
        print("\nStep 1: Testing Iframe Interaction...")
        # Using the direct TinyMCE URL which is more stable for automation
        self.driver.get("https://the-internet.herokuapp.com/tinymce")
        self.page.handle_iframe("Hello! Context switching successful.")

        # Task 3, 4, & 5: Windows
        print("\nStep 2: Testing Window Switching...")
        self.driver.get("https://the-internet.herokuapp.com/windows")
        self.page.handle_windows()
        
        print("\nResult: PASS - All contexts handled.")

    def tearDown(self):
        self.driver.quit()
        if hasattr(sys.stdout, 'log'):
            sys.stdout.log.close()

if __name__ == "__main__":
    unittest.main()