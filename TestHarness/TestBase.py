from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


class TestBase:
    applicationURI = ''

    def __init__(self, driver):
        self.driver = driver


def openSession(self, browser):
    if browser == 'chrome':
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        self.driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        chromeOptions = Options()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument('--window-size=1920x1080')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)


def closeSession(self):
    if self.driver is not None:
        self.driver.close()
        self.driver.quit()


def redirectTo(self, URI):
    self.driver.get(URI)
