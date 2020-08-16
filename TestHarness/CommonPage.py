from TestHarness.TestBase import TestBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

wdWait = 10


class CommonPage(TestBase):
    def __init__(self, driver):
        self.driver = driver


def expliciteWait(self, elementToBeWait):
    element = WebDriverWait(self.driver, wdWait).until(ec.presence_of_element_located(elementToBeWait))
