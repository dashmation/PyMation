from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://jqueryui.com/droppable/')
time.sleep(3)
try:
    # right Click or Context Click
    droppable_Heading = driver.find_element(By.CLASS_NAME, 'entry-title')
    performAction = ActionChains(driver)
    performAction.context_click(droppable_Heading).perform()
except Exception as e:
    print("Unable to perform due to:", e)
time.sleep(5)
driver.quit()
