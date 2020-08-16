from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.spicejet.com/')
time.sleep(3)
# move to element
try:
    driver.implicitly_wait(20)
    # WebElement
    login_SignUp = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
    performAction = ActionChains(driver)
    performAction.move_to_element(login_SignUp).perform()
    # WebElement
    spiceClub_Members = driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
    performAction.move_to_element(spiceClub_Members).perform()
    # WebElement
    member_Login = driver.find_element(By.LINK_TEXT, 'Member Login')
    member_Login.click()
except Exception as e:
    print('Unable to perform due to:', e)
time.sleep(2)
print('Current URI is:', driver.current_url)
print('Current Title is:', driver.title)
driver.quit()
