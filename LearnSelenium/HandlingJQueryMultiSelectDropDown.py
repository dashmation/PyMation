from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/')

mul_DropDown = driver.find_element(By.ID, 'justAnInputBox')
drop_Down_Items = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')


def selectOne(elements, value):
    for items in elements:
        if items.text.strip() != '':
            print(items.text)
            if items.text.strip() == value:
                items.click()
                print('===============================')
                print(items.text, " selected")
                print('===============================')
                break


def selectMultiple(elements, values):
    try:
        if values[0].lower() != 'all':
            for ele in elements:
                for items in range(len(values)):
                    if ele.text.strip() == values[items]:
                        ele.click()
                        print('===============================')
                        print(ele.text, " selected")
                        print('===============================')
                        break
        else:
            for ele in elements:
                if ele.text.strip() != '':
                    ele.click()
                    print('===============================')
                    print(ele.text, " selected")
                    print('===============================')
    except Exception as e:
        print(e)


mul_DropDown.click()
selectOne(drop_Down_Items, 'choice 1')
selectOne(drop_Down_Items, 'choice 2')
selectOne(drop_Down_Items, 'choice 3')
time.sleep(3)
listOfValues = ['All']
selectMultiple(drop_Down_Items, listOfValues)
driver.quit()
