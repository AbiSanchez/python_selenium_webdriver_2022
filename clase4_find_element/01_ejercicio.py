import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Inicializar driver
chrome_driver_path = 'drivers/chromedriver'
gecko_driver_path = 'drivers/geckodriver'
url = 'https://laboratorio.qaminds.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Abrir pagina
driver.get(url)

# busqueda en web
barra : WebElement = driver.find_element(By.XPATH,'//*[@id="search"]/input')
assert barra.is_displayed(), 'No se encuentra'
barra.send_keys('iphone')
boton_buscar : WebElement = driver.find_element(By.XPATH,'//*[@id="search"]/input')
assert boton_buscar.is_displayed(), 'No se encuentra boton'
boton_buscar.click()
time.sleep(5)

iphone : WebElement =driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div/div/div[1]/a/img')  #TODO - MEJORAR XPATH
assert iphone.is_displayed(), 'No se encuentra imagen de iphone'

# Cerrar navegador
driver.quit()