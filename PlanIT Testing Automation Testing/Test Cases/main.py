import unittest
from selenium import webdriver
import page

class TestCases(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Edge("msedgedriver.exe")
        self.driver.get("https://jupiter.cloud.planittesting.com/#/")

    def test_case1(self):
        main_page = page.MainPage(self.driver)
        main_page.click_contact_button()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()