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


class TestDisplay:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())

    def test_search_display(self):
        # Open web page
        self.driver.get("https://laboratorio.qaminds.com/")

        # Search_bar
        search_loc = (By.XPATH,'//*[@id="search"]/input')
        search_textbox : WebElement = self.wait.until(EC.presence_of_element_located(search_loc))
        search_textbox.clear()
        search_textbox.send_keys("Display")
        
        # Search_button
        search_btn_loc = (By.CLASS_NAME,'input-group-btn')
        search_btn : WebElement = self.wait.until(EC.element_to_be_clickable(search_btn_loc))
        search_btn.click()
        
        # Search_response
        search_response_loc = (By.XPATH,'//*[@id="content"]/p[2]')
        # search_response : WebElement = 
        assert self.wait.until(EC.text_to_be_present_in_element(search_response_loc,'There is no product that matches the search criteria'))

        # Option_search in products
        check_prod_loc = (By.ID,'description')
        check_prod : WebElement = self.wait.until(EC.element_to_be_clickable(check_prod_loc))
        check_prod.click()
        
        # boton search
        search_btn_loc2 = (By.CLASS_NAME,'btn-primary')
        search_btn2 : WebElement = self.wait.until(EC.element_to_be_clickable(search_btn_loc2))
        search_btn2.click()       
        
        # apple cinema
        apple_cine_loc = (By.LINK_TEXT,'Apple Cinema 30"')
        apple_cine : WebElement = self.wait.until(EC.element_to_be_clickable(apple_cine_loc))
        assert apple_cine.is_displayed(), 'apple cinema not found'

        # ipod nano
        ipod_nano_loc = (By.LINK_TEXT,'Apple Cinema 30"')
        ipod_nano : WebElement = self.wait.until(EC.element_to_be_clickable(ipod_nano_loc))
        assert ipod_nano.is_displayed(), 'ipod nano not found'

        # ipod touch
        ipod_touch_loc = (By.LINK_TEXT,'Apple Cinema 30"')
        ipod_touch : WebElement = self.wait.until(EC.element_to_be_clickable(ipod_touch_loc))
        assert ipod_touch.is_displayed(), 'ipod touch not found'

        # macbook
        macbook_loc = (By.LINK_TEXT,'Apple Cinema 30"')
        macbook : WebElement = self.wait.until(EC.element_to_be_clickable(macbook_loc))
        assert macbook.is_displayed(), 'macbook not found'            
  
   

    def teardown_method(self):
        if self.driver:
            self.driver.quit()