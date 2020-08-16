from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initializing Chrome Driver
driver = webdriver.Chrome(executable_path='D:\\Softwares\\chromedriver_win32\\chromedriver.exe')
# Maximizing Browser
driver.maximize_window()
# Implicit wait
driver.implicitly_wait(5)
# Browsing URI
driver.get("https://google.co.in")
# Getting Title Of The Page
print('Title is '+driver.title)
# Entering into textbox using sendKeys using By.name
driver.find_element(By.NAME, 'q').send_keys("selenium")
# Getting Text and Clicking on particular Suggested Name using list
listOfSuggestions = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
for suggestedElement in listOfSuggestions:
    extractedText = suggestedElement.text
    if extractedText != "":
        print('Suggestions are ', extractedText)
    if extractedText == 'selenium testing':
        suggestedElement.click()
        break


# Thread.sleep in Java
time.sleep(1)
# Browser quit
driver.quit()

