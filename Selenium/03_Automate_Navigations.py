from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com')

search = driver.find_element(By.NAME, 'q')
search.send_keys('selenium' + Keys.RETURN)

time.sleep(20)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)



