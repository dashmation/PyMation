from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.facebook.com/')


def selectDropDownUsing(selectElement, SelectByValue):
    select = Select(selectElement)
    select.select_by_value(SelectByValue)


def deSelectDropDownUsing(selectElement, SelectByValue):
    select = Select(selectElement)
    select.deselect_by_value(SelectByValue)


def isMultiple(selectElement):
    select = Select(selectElement)
    return select.is_multiple


def printAllTheListItems(selectElement):
    select = Select(selectElement)
    listOfItems = select.options
    for items in listOfItems:
        print(items.text)


def selectItemFrom(selectElement, valueToBeSelected):
    select = Select(selectElement)
    listOfItems = select.options
    for items in listOfItems:
        if items.text == valueToBeSelected:
            items.click()
            break


# select without using select
def selectWithoutSelect(xpathExpression, valueToBeSelected):
    listOfItems = driver.find_elements(By.XPATH, xpathExpression)
    for items in listOfItems:
        if items.text == valueToBeSelected:
            items.click()
            break


day_DropDown = driver.find_element(By.ID, 'day')
month_DropDown = driver.find_element(By.ID, 'month')
year_DropDown = driver.find_element(By.ID, 'year')

# selecting
selectDropDownUsing(day_DropDown, '4')
selectDropDownUsing(month_DropDown, '7')
selectDropDownUsing(year_DropDown, '1991')

print(isMultiple(day_DropDown))
print(isMultiple(month_DropDown))
print(isMultiple(year_DropDown))

# Deselecting
try:
    deSelectDropDownUsing(day_DropDown, '4')
    deSelectDropDownUsing(month_DropDown, '7')
    deSelectDropDownUsing(year_DropDown, '1991')
except Exception as e:
    print(e, ' found')

printAllTheListItems(month_DropDown)

selectItemFrom(month_DropDown, 'Jun')

selectWithoutSelect(".//*[@id='month']/option", 'Dec')

time.sleep(5)
driver.quit()
