from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('http://www.amazon.in')
driver.maximize_window()

time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys('iphones')

driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()

time.sleep(5)