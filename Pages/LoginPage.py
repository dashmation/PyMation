from self import self

from TestHarness.CommonPage import CommonPage
from selenium.webdriver.common import By


class LoginPage(CommonPage):
    self.username_TextBox = By.ID()

    def __int__(self, driver):
        self.driver = driver

