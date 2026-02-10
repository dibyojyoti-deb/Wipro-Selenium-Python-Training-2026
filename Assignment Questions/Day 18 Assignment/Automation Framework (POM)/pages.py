from base_page import BasePage
from locators import InventoryLocators

class LoginPage(BasePage):
    def login(self, username, password):
        self.input_text(InventoryLocators.USERNAME_FIELD, username)
        self.input_text(InventoryLocators.PASSWORD_FIELD, password)
        self.save_evidence("Screenshot1_LoginFilled")
        self.click(InventoryLocators.LOGIN_BUTTON)

class InventoryPage(BasePage):
    def get_header(self):
        header = self.get_text(InventoryLocators.PRODUCT_HEADER)
        self.save_evidence("Screenshot2_Dashboard")
        return header