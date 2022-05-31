from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage
from lib.pom.qaminds.product_page import ProductPage
from lib.pom.qaminds.checkout_page import CheckoutPage


class TestFinalCheckoutPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        
    def test_shopping_cart_empty(self):
        self.checkout_page.checkout_btn()
        assert self.checkout_page.get_page_title() == 'Shopping Cart'
        assert self.checkout_page.get_message_empty() == 'Your shopping cart is empty!'
        self.checkout_page.btn_continue_empty()


    def test_form_checkup(self):
        product = 'iPhone'
        self.home_page.search(product)
        self.home_page.select_product('iPhone')
        self.product_page.add_to_cart()
        self.checkout_page.checkout_btn()
        assert self.checkout_page.get_page_title() == 'Checkout'
        assert self.checkout_page.title_first_form_visible() == "New Customer"
        assert self.checkout_page.radio_btn_register_is_selected() , 'No se encuentra seleccionado'
        self.checkout_page.btn_continue_in_form()
        assert self.checkout_page.title_second_form_visible() == "Your Personal Details"

                  

    def teardown_method(self):
        if self.driver:
            self.driver.quit()