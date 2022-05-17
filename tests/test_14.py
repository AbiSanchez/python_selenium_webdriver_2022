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


class TestDesktop:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())

    def test_search_desktop(self):
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

        # desktop
        desktop_loc = (By.LINK_TEXT,'Desktops')
        desktop : WebElement = self.wait.until(EC.element_to_be_clickable(desktop_loc))
        assert desktop.is_displayed(), 'desktopss not found'
        desktop.click()

        
        # mac
        mac_loc = (By.PARTIAL_LINK_TEXT,'Mac')
        mac : WebElement = self.wait.until(EC.element_to_be_clickable(mac_loc))
        assert mac.is_displayed(), 'mac dropdown not found'  
        mac.click()

        # imac
        imac_loc = (By.LINK_TEXT,'iMac')
        imac : WebElement = self.wait.until(EC.element_to_be_clickable(imac_loc))
        assert imac.is_displayed(), 'iMac not found'  
        imac.click()

        # agregarlo al carrito
        agregar_loc = (By.ID, 'button-cart')
        agregar : WebElement = self.wait.until(EC.element_to_be_clickable(agregar_loc))
        assert agregar.is_displayed(), 'iMac not found'  
        agregar.click()

        # total del carrito
        car_tot_loc = (By.ID, 'cart-total')
        assert self.wait.until(EC.text_to_be_present_in_element(car_tot_loc,"1 item(s) - $122.00"))
     

    
    def teardown_method(self):
        if self.driver:
            self.driver.quit()