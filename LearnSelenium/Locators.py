from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
import time

# enter Browser name
browsername = input("Please Enter The Browsername: ")
if (browsername != 'chrome') and (browsername != 'firefox') and (browsername != 'headless'):
    browsername = 'headless'
    print('Launching ', browsername)

# Launching browser using webdriver manager
if browsername == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browsername == 'headless':
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.facebook.com/')

emailOrPhone = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'pass')
logIn = driver.find_element(By.ID, 'u_0_b')

emailOrPhone.send_keys('rkwrnrw')
password.send_keys('$&@*$*&#')
logIn.click()

loginbutton = driver.find_element(By.ID, 'loginbutton')
if loginbutton.is_displayed():
    print('Element displayed')
else:
    AssertionError

driver.close()
