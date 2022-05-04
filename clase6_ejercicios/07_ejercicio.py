from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Setup
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)

locator2 = (By.ID, 'at-cv-lightbox-close')
search_close: WebElement = wait.until(EC.element_to_be_clickable(locator2))
search_close.click()

driver.quit()

