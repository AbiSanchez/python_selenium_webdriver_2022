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
url = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 7)

# Open Web Page
driver.get(url)

# Boton autoclosable
locator = (By.ID, 'autoclosable-btn-success')
start_download: WebElement = wait.until(EC.element_to_be_clickable(locator))
assert start_download.is_displayed(),'Boton no se muestra'
start_download.click()

# mensaje
locator2 =(By.CSS_SELECTOR,'.alert-autocloseable-success')
assert wait.until(EC.visibility_of_element_located(locator2)), 'No se muestra el mensaje'
time.sleep(5)
assert wait.until(EC.invisibility_of_element_located(locator2)), 'Se muestra el mensaje'


# close browser
driver.quit()