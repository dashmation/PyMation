from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(3)
try:
    driver.implicitly_wait(10)
    username_TextBox = driver.find_element(By.ID, 'txtUsername')
    password_TextBox = driver.find_element(By.ID, 'txtPassword')
    login_Button = driver.find_element(By.ID, 'btnLogin')
    performAction = ActionChains(driver)
    performAction.send_keys_to_element(username_TextBox, 'Admin').perform()
    performAction.send_keys_to_element(password_TextBox, 'admin123')
    performAction.click(login_Button).perform()
except Exception as e:
    print('Unable to perform due to:', e)
time.sleep(5)
print(driver.title)
driver.quit()
