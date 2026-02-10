from selenium.webdriver.common.by import By

class InventoryLocators:
    # Example using a standard demo site (SauceDemo)
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCT_HEADER = (By.CLASS_NAME, "title")