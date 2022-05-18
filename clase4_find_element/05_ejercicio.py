import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement   # Init Browsers
from selenium.webdriver.support.select import Select


chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = "https://demoqa.com/select-menu"
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

# Open Web Page
driver.get(url)

# Test Logic
time.sleep(2)
colors = driver.find_element(By.ID, "oldSelectMenu")
assert colors.is_displayed(), "Colors is not visible"
colors_dropdown = Select(colors)
colors_dropdown.select_by_visible_text("Green")
selected_option: WebElement = colors_dropdown.first_selected_option
assert selected_option.text == "Green", "Green is not selected"

driver.quit()