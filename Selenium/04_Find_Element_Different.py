from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com')

search = driver.find_element(By.NAME, 'q')
search.send_keys('selenium')

wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'gNO89b')))
button.click()

input("Press Enter to close the browser...")
driver.quit()