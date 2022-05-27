from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage
from lib.pom.qaminds.product_page import ProductPage


class TestFinalHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        
    def test_menu(self):   #VALIDACION SUBMENU
        # 1. Abrir explorador
        # 2. Ir a la URL
        # 3. Dar click al menu components -> monitors
        # 4. Seleccionar el producto Apple Cinema 30"
        # 4. Validar que se muestre el producto Apple Cinema 30"
        self.home_page.select_sub_menu('Components','Monitors')
        self.home_page.select_product('Apple Cinema 30"')
        assert self.product_page.get_name() == 'Apple Cinema 30"'
        
 
    def test_car_total(self):       #VALIDACION CARRITO DE COMPRAS
        # 1. Abrir el explorador
        # 2. Ir a la URL
        # 3. Identificar el elemento de carrito de comparas y validar que el valor del carrito de comparas sea "0 item(s) - $0.00"
        total = self.home_page.get_cart_total()
        assert "0 item(s) - $0.00" == total        

    def test_currency(self):       #VALIDACION DE MONEDA
        # 1. Abrir explorador
        # 2. Ir a la URL
        # 3. Identificar el elemento de currency y validar que se muestre el "$" de USD
        currency = self.home_page.get_currency()
        assert currency == '$'
        

    def teardown_method(self):
        if self.driver:
            self.driver.quit()