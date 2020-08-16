from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
import time

# browserType = input("Please enter Browser: ")


def launchChrome():
    driver = webdriver.Chrome(ChromeDriverManager().install())


def launchFirefox():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def launchHeadless():
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)


def launchBroswer(arguement):
    if arguement == 'chrome' or 'firefox' or 'headless':
        switcher = {
            'chrome': launchChrome(),
            'firefox': launchFirefox(),
            'headless': launchHeadless()
        }
    else:
        print('Please enter valid browserType')


launchBroswer(input("Please enter Browser: "))
