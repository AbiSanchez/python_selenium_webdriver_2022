from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage
from lib.pom.qaminds.product_page import ProductPage


class TestFinalSearchPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        
    def test_existing_product(self):
        product = 'iPhone'
        self.home_page.search(product)
        assert self.home_page.product_visible(product) == product
        
    def test_nonexisting_product(self):
        product = 'iPhones'
        self.home_page.search(product)
        assert self.home_page.product_no_visible(), 'El mensaje de Error no se muestra'
 
          

    def teardown_method(self):
        if self.driver:
            self.driver.quit()