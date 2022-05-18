from multiprocessing.connection import wait
from xml.sax.xmlreader import Locator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config
import time


class TestSamsumg:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

    def test_currency(self):
        
        # USD  default
        usd_loc = (By.XPATH,'//*[@id="form-currency"]/div/button/strong')
        assert self.wait.until(EC.text_to_be_present_in_element(usd_loc,'$'))

        # Search_bar
        search_loc = (By.XPATH,'//*[@id="search"]/input')
        search_textbox : WebElement = self.wait.until(EC.presence_of_element_located(search_loc))
        search_textbox.clear()
        search_textbox.send_keys("Samsung")
        
        # Search_button
        search_btn_loc = (By.CLASS_NAME,'input-group-btn')
        search_btn : WebElement = self.wait.until(EC.element_to_be_clickable(search_btn_loc))
        search_btn.click()

        # Samsung SyncMaster 941BW link
        samsung_loc = (By.LINK_TEXT,'Samsung SyncMaster 941BW')
        samsung : WebElement = self.wait.until(EC.element_to_be_clickable(samsung_loc))
        assert samsung.is_displayed(), 'Samsung SyncMaster 941BW not found'  
        samsung.click()

        #Precio USD
        precio_loc = (By.XPATH,'//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2')
        precio_usd : WebElement = self.wait.until(EC.visibility_of_element_located(precio_loc))
        value_usd = float (precio_usd.text[1:])
        
        #Dropdown currency
        currency_loc = (By.XPATH,'//*[@id="form-currency"]/div/button')
        drop_currency: WebElement = self.wait.until(EC.element_to_be_clickable(currency_loc))
        drop_currency.click()

        #Cambiar Euros
        euro_currency_loc = (By.NAME, 'EUR')
        euro_currency : WebElement = self.wait.until(EC.element_to_be_clickable(euro_currency_loc))
        euro_currency.click()

        # Precio EUROS
        precio_eur : WebElement = self.wait.until(EC.visibility_of_element_located(precio_loc))
        value_eur = float(precio_eur.text[:-1])

        print ('###############')
        print (value_usd)
        print (value_eur)

        assert value_eur < value_usd


    def teardown_method(self):
        if self.driver:
            self.driver.quit()