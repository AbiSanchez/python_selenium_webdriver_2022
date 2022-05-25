from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.product_page import ProductPage


class TestProductPage:
    driver: WebDriver = None
    product_page: ProductPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.product_page = ProductPage(self.driver)
        self.product_page.goto("https://laboratorio.qaminds.com/index.php?route=product/product&product_id=33&search=s amsung")

    def test_get_product_information(self):
        description = """Imagine the advantages of going big without slowing down. The big 19" 941BW monitor combines wide aspect ratio with fast pixel response time, for bigger images, more room to work and crisp motion. In addition, the exclusive MagicBright 2, MagicColor and MagicTune technologies help deliver the ideal image in every situation, while sleek, narrow bezels and adjustable stands deliver style just the way you want it. With the Samsung 941BW widescreen analog/digital LCD monitor, it's not hard to imagine."""
        assert self.product_page.get_name() == 'Samsung SyncMaster 941BW'
        assert self.product_page.get_description() == description
        assert self.product_page.get_price() == '$242.00'
        assert self.product_page.get_ex_tax() == '$200.00'
        assert self.product_page.get_product_code() == 'Product 6'
        assert self.product_page.get_availability() == 'In Stock'

    def test_add_to_cart(self):
        self.product_page.add_to_cart()

    def test_get_total_reviews(self):
        assert self.product_page.get_total_reviews() == '0'

    def teardown_method(self):
        if self.driver:
            self.driver.quit()