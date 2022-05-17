from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config
import time


class TestDownload:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())

    def test_download_button_1(self):
        """Ejercicio 8"""
        # Open web page
        self.driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

        # Click download
        download_loc = (By.ID, "downloadButton")
        download: WebElement = self.wait.until(EC.element_to_be_clickable(download_loc))
        download.click()

        # Verify progress label
        progress_label_loc = (By.CLASS_NAME, "progress-label")  # XPATH: //*[@class='progress-label']
        self.wait.until(EC.text_to_be_present_in_element(progress_label_loc, "Complete!"))

        # Verify continue button
        close_btn_local = (By.XPATH, "//button[text()='Close']")
        close_btn: WebElement = self.wait.until(EC.element_to_be_clickable(close_btn_local))
        close_btn.click()

    def test_download_button_2(self):
        """Ejercicio 9"""
                
        # Open web page
        self.driver.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")
        
        # Boton descargar
        locator = (By.ID, 'cricle-btn')
        start_download: WebElement = self.wait.until(EC.element_to_be_clickable(locator))
        assert start_download.is_displayed(),'Boton no se muestra'
        start_download.click()
        # descarga 100%
        time.sleep(15)
        locator2 =(By.CLASS_NAME,'percenttext')
        assert self.wait.until(EC.text_to_be_present_in_element(locator2,'100%')), 'No se muestra el texto'
        


    def test_auto_closable_msg(self):
        """Ejercicio 10"""

        # Open web page
        self.driver.get("https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html")

        # Boton autoclosable
        locator = (By.ID, 'autoclosable-btn-success')
        start_download: WebElement = self.wait.until(EC.element_to_be_clickable(locator))
        assert start_download.is_displayed(),'Boton no se muestra'
        start_download.click()

        # mensaje
        locator2 =(By.CSS_SELECTOR,'.alert-autocloseable-success')
        assert self.wait.until(EC.visibility_of_element_located(locator2)), 'No se muestra el mensaje'
        time.sleep(5)
        assert self.wait.until(EC.invisibility_of_element_located(locator2)), 'Se muestra el mensaje'        

    def teardown_method(self):
        if self.driver:
            self.driver.quit()