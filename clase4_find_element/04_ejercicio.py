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

laptop_notebook = driver.find_element(By.LINK_TEXT, 'Laptops & Notebooks')
assert laptop_notebook.is_displayed(), 'Laptops & Notebooks no se muestran'
laptop_notebook.click()

time.sleep(5)
windows_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Windows')
assert windows_link.is_displayed(),'Windows no se muestra'
windows_link.click()

msg_label = driver.find_element(By.XPATH, '//*[@id="content"]/p')
assert msg_label.is_displayed(), 'el mensaje no es visible'
assert msg_label.text == 'There are no products to list in this category.', 'El mensaje no se muestra'

time.sleep(5)
continue_btn = driver.find_element(By.LINK_TEXT,'Continue')
assert continue_btn.is_displayed(), 'Error'
continue_btn.click()

driver.quit()