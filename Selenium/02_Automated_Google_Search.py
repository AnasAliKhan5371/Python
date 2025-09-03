"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get('http://www.google.com')

input = driver.find_element(By.NAME, 'q')
input.send_keys('selenium')
time.sleep(5) #seconds
button = driver.find_element(By.NAME, 'btnk')
button.click()
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com')

search = driver.find_element(By.NAME, 'q')
search.send_keys('selenium' + Keys.RETURN)
input("Press Enter to close the browser...")
driver.quit()