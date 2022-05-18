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

# Buscar tablets
tablets = driver.find_element(By.LINK_TEXT,'Tablets')
assert tablets.is_displayed(),'Tablets no se encuenta'
tablets.click()


time.sleep(5)
samsung = driver.find_element(By.LINK_TEXT,'Samsung Galaxy Tab 10.1')
assert samsung.is_displayed(), 'Samsung no se encuentra'
samsung.click()

precio = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2')
assert precio.is_displayed() , 'El precio no se muestra'
assert precio.text == '$241.99', 'El precio no coincide con $241.99'

wish_list_btn = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div[1]/button[1]')
assert wish_list_btn.is_displayed(), "El boton Whish list no se muestra"
wish_list_btn.click()

add_carrito= driver.find_element(By.ID,'button-cart')
assert add_carrito.is_displayed(), 'Boton add no es visible'
add_carrito.click()

# Close Browser
driver.quit()