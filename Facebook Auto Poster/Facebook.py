#anasalikhan991@gmail.com
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.facebook.com/')

email=driver.find_element(By.XPATH,'//*[@id="email"]')
email.send_keys('anasalikhan991@gmail.com')

password=driver.find_element(By.XPATH,'.//*[@id="pass"]')
password.send_keys('Anas5371***'+ Keys.RETURN)

time.sleep(70)

wait = WebDriverWait(driver, 5)
whats_on_your_mind = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), \"What's on your mind, Anas?\")]"))
    )
    # Click on the input area to activate it
whats_on_your_mind.click()

time.sleep(4)


post_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
    )
post_input.send_keys("Hello, this is an automated test post!")

post=driver.find_elements(By.XPATH,'//*[@aria-label="Post"]')

for button in post:
    if button.text=='Post':
        button.click()

input("Press Enter to close the browser...")
driver.quit()