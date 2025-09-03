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

list=driver.find_elements(By.XPATH,"//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")

print(str(len(list)) + ' products found')

for i in list:
    print(i.text)

driver.quit()