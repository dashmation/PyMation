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
    driver.implicitly_wait(5)
    frame = driver.find_element(By.CLASS_NAME, 'demo-frame')
    driver.switch_to.frame(frame)
    source = driver.find_element(By.ID, 'draggable')
    target = driver.find_element(By.ID, 'droppable')
    performAction = ActionChains(driver)
    # Using drag and drop
    performAction.drag_and_drop(source, target).perform()
    # ====================OR============================
    # Using click and hold then release
    performAction.click_and_hold(source).move_to_element(target).release(target).perform()
except Exception as e:
    print('Unable to perform due to:', e)
time.sleep(3)
driver.quit()
