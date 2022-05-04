from selenium.webdriver.common.by import By

class MainPageLocators(object):

    BRAND_BUTTON = (By.CLASS_NAME, 'brand')
    HOME_BUTTON = (By.ID, 'nav-home')
    SHOP_BUTTON = (By.ID, 'nav-shop')
    CONTACT_BUTTON = (By.ID, 'nav-contact')
    LOGIN_BUTTON = (By.ID, 'nav-login')
    CART_BUTTON = (By.ID, 'nav-cart')
    START_SHOP_BUTTON = (By.CLASS_NAME, 'btn btn-success btn-large')
