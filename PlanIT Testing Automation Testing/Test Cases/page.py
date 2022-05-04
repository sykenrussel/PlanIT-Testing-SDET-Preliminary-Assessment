from element import BasePageElement
from locators import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def click_brand_button(self):
        element = self.driver.find_element(*MainPageLocators.BRAND_BUTTON)
        element.click()

    def click_home_button(self):
        element = self.driver.find_element(*MainPageLocators.HOME_BUTTON)
        element.click()

    def click_shop_button(self):
        element = self.driver.find_element(*MainPageLocators.SHOP_BUTTON)
        element.click()

    def click_contact_button(self):
        element = self.driver.find_element(*MainPageLocators.CONTACT_BUTTON)
        element.click()

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def click_cart_button(self):
        element = self.driver.find_element(*MainPageLocators.CART_BUTTON)
        element.click()

    def click_start_shop_button(self):
        element = self.driver.find_element(*MainPageLocators.START_SHOP_BUTTON)
        element.click()
