import email
import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement   # Init Browsers


chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = "https://laboratorio.qaminds.com/"
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get(url)
time.sleep(5)

# Login
my_account = driver.find_element(By.LINK_TEXT, 'My Account')
assert my_account.is_displayed(), 'My account no se muestra'
my_account.click()

time.sleep(2)
login_link = driver.find_element(By.LINK_TEXT,'Login')
assert login_link.is_displayed(), 'Login no se muestra'
login_link.click()

# datos email y password
time.sleep(2)
email_box = driver.find_element(By.ID,'input-email')
assert email_box.is_displayed(),'Email box no se muestra'
email_box.clear()
email_box.send_keys('CORREO_ERROR')

password = driver.find_element(By.ID, 'input-password')
assert password. is_displayed(), 'Password no es visible'
password.clear()
password.send_keys('ERROR')

# boton de login
login_btn =driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
assert  login_btn.is_displayed(),'No es visible'
login_btn.click()

# Error
error_msg = driver.find_element(By.XPATH,'//*[@id="account-login"]/div[1]')
assert error_msg.is_displayed(),'El error no se muestra'

# Close Browser
driver.quit()
