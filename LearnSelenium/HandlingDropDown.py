from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.facebook.com/')

# Init WebElements
day_DropDown = driver.find_element(By.ID, 'day')
month_DropDown = driver.find_element(By.ID, 'month')
year_DropDown = driver.find_element(By.ID, 'year')

# Init Select For Day DropDown
select_Day = Select(day_DropDown)
# Select Day By Index
select_Day.select_by_index(5)
# Select Day By Value
select_Day.select_by_value('3')
# Select Day By Visible Text
select_Day.select_by_visible_text('4')

# Init Select For Month DropDown
select_Month = Select(month_DropDown)
# Select Month By Index
select_Month.select_by_index(10)
# Select Month By Value
select_Month.select_by_value('4')
# Select Month By Visible Text
select_Month.select_by_visible_text('Jul')

# Init Select For Year DropDown
select_Year = Select(year_DropDown)
# Select Year By Index
select_Year.select_by_index(12)
# Select Year By Value
select_Year.select_by_value('1980')
# Select Year By Visible Text
select_Year.select_by_visible_text('1991')

driver.quit()
