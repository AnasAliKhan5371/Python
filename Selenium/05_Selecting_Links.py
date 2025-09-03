from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://www.amazon.in')
driver.maximize_window()

time.sleep(5)

select = driver.find_element(By.LINK_TEXT, 'Mobiles')
select.click()

time.sleep(5)

select = driver.find_element(By.LINK_TEXT, 'Audio')
select.click()

time.sleep(5)


