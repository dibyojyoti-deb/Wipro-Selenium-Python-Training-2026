from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import time
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    # Locators
    REGISTER_LINK = (By.CLASS_NAME, "ico-register")
    LOGOUT_LINK = (By.CLASS_NAME, "ico-logout")
    WISHLIST_LINK = (By.CLASS_NAME, "ico-wishlist")
    CART_LINK = (By.CLASS_NAME, "ico-cart")
    SEARCH_BOX = (By.ID, "small-searchterms")
    SEARCH_BTN = (By.CSS_SELECTOR, ".search-box-button")
    CURRENCY_DROPDOWN = (By.ID, "customerCurrency")
    HOME_LOGO = (By.XPATH, "//div[@class='header-logo']//img")
    
    # Sort/Display Locators
    SORT_DROPDOWN = (By.ID, "products-orderby")
    SIZE_DROPDOWN = (By.ID, "products-pagesize")
    
    # Footer Links
    LINK_SITEMAP = (By.LINK_TEXT, "Sitemap")
    LINK_SHIPPING = (By.LINK_TEXT, "Shipping & returns")
    LINK_PRIVACY = (By.LINK_TEXT, "Privacy notice")
    LINK_ABOUT = (By.LINK_TEXT, "About us")
    LINK_CONTACT = (By.LINK_TEXT, "Contact us")

    def nav_to_home(self):
        if self.is_visible(self.HOME_LOGO):
            self.click_element(self.HOME_LOGO)
        else:
            self.driver.get("https://demo.nopcommerce.com/")

    def nav_to_register(self):
        self.click_element(self.REGISTER_LINK)

    def nav_to_cart(self):
        self.click_element(self.CART_LINK)

    def nav_to_wishlist(self):
        # Replaced standard .click() with our robust JS-powered click_element
        # This will completely bypass the green notification bar if it is still open
        self.click_element(self.WISHLIST_LINK)

    def logout(self):
        if self.is_visible(self.LOGOUT_LINK):
            self.click_element(self.LOGOUT_LINK)

    def search_for_product(self, query):
        # 1. Use your robust BasePage method to guarantee the text is entered
        self.enter_text(self.SEARCH_BOX, query)
        time.sleep(0.5)
        
        # 2. Force the JavaScript click
        btn = self.wait.until(EC.presence_of_element_located(self.SEARCH_BTN))
        self.driver.execute_script("arguments[0].click();", btn)
        
        # 3. Safety net: If Chrome types too fast and triggers the empty search alert, dismiss it
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass

    def switch_currency(self, currency_name):
        elem = self.wait.until(EC.visibility_of_element_located(self.CURRENCY_DROPDOWN))
        Select(elem).select_by_visible_text(currency_name)

    def sort_products(self, sort_text):
        elem = self.wait.until(EC.visibility_of_element_located(self.SORT_DROPDOWN))
        Select(elem).select_by_visible_text(sort_text)
        
    def change_display_size(self, size_text):
        elem = self.wait.until(EC.visibility_of_element_located(self.SIZE_DROPDOWN))
        Select(elem).select_by_visible_text(size_text)