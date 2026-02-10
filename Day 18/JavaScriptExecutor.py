from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

time.sleep(5)

driver.execute_script("window.scrollBy(0, 900);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)
driver.quit()