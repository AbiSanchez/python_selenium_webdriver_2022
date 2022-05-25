from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage


class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test(self):
        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'
        home_page.search('Samsung')

    def test_menu(self):
        #  1. Dar click al menu de tablets
        #  2. Dar click al menu de software
        home_page = HomePage(self.driver)
        home_page.select_menu('Tablets')
        home_page.select_menu('Software')
        
    def test_sub_menu(self):
        #  1. Dar click al menu components -> monitors
        #  2. Seleccionar Apple Cinema 30"
        home_page = HomePage(self.driver)
        home_page.select_sub_menu('Components','Monitors')
        home_page.select_product('Samsung SyncMaster 941BW')
        

    def test_currency(self):
        #  1. Verificar currency, debe ser igual a $
        #  2. Cambiar currency a euros
        home_page = HomePage(self.driver)
        currency = home_page.get_currency()
        assert currency == '$'
        home_page.set_currency("EUR")
        assert "€" == home_page.get_currency()


    def test_cart(self):
        # 1. Verificar texto en carro de compra, valor esperado: 0 item(s) - $0.00
        home_page = HomePage(self.driver)
        total = home_page.get_cart_total()
        assert "0 item(s) - $0.00" == total        

    def teardown_method(self):
        if self.driver:
            self.driver.quit()