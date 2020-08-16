from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
import time

# enter Browser name
browsername = input("Please Enter The Browsername: ")

if browsername.strip() != 'chrome' and browsername.strip() != 'firefox' and browsername.strip() != 'edge':
    browsername = 'headless'
keyword = input("Please Enter The keyword: ")
getKeyword = input("Please Enter The getKeyword: ")
print(' Entered browsername:', browsername, '\n', 'Entered keyword:', keyword, '\n', 'Entered getKeyword:', getKeyword)
time.sleep(2)
# Launching browser using webdriver manager
if browsername == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == 'headless':
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)
elif browsername == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # raise Exception()
elif browsername == 'edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    # raise Exception()

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.google.co.in")
print('Title is ' + driver.title)
driver.find_element(By.NAME, 'q').send_keys(keyword)
listOfSuggestions = driver.find_elements(By.CSS_SELECTOR, "ul.erkvQe li span")
i = 1
for suggestedElement in listOfSuggestions:
    extractedText = suggestedElement.text
    if extractedText != "":
        print('Suggestions are ', i, "", extractedText)
        i = i + 1
    if extractedText.find(getKeyword):
        suggestedElement.click()
        break
time.sleep(1)
driver.quit()
