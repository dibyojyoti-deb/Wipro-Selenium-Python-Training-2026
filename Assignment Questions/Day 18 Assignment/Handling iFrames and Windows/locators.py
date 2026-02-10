from selenium.webdriver.common.by import By

class SwitchLocators:
    # Iframe Example (TinyMCE or similar)
    IFRAME_ID = "mce_0_ifr"
    IFRAME_BODY = (By.ID, "tinymce")
    
    # Window Example
    NEW_WINDOW_BUTTON = (By.LINK_TEXT, "Click Here")