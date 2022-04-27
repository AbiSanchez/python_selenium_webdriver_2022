# Librerias para ejecutar el script

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#paths de los drivers

chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'

# url que va abrir

url = 'https://qamindslab.com'
service = Service(chrome_driver_path)

# Codigo para abrir y cerrar el navegador.

driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(3)
driver.quit()