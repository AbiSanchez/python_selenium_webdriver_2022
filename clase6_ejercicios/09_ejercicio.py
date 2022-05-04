from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# Setup
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15)

# Open Web Page
driver.get(url)

# Boton descargar
locator = (By.ID, 'cricle-btn')
start_download: WebElement = wait.until(EC.element_to_be_clickable(locator))
assert start_download.is_displayed(),'Boton no se muestra'
start_download.click()

# descarga 100%
time.sleep(15)
locator2 =(By.CLASS_NAME,'percenttext')
assert wait.until(EC.text_to_be_present_in_element(locator2,'100%')), 'No se muestra el texto'

# close browser
driver.quit()