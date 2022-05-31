from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.product_page import ProductPage


class TestFinalProductPage:
    driver: WebDriver = None
    product_page: ProductPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.product_page = ProductPage(self.driver)
        self.product_page.goto("https://laboratorio.qaminds.com/index.php?route=product/product&path=57&product_id=49")

    def test_get_product_information(self):
        description = """Samsung Galaxy Tab 10.1, is the world’s thinnest tablet, measuring 8.6 mm thickness, running with Android 3.0 Honeycomb OS on a 1GHz dual-core Tegra 2 processor, similar to its younger brother Samsung Galaxy Tab 8.9.\nSamsung Galaxy Tab 10.1 gives pure Android 3.0 experience, adding its new TouchWiz UX or TouchWiz 4.0 – includes a live panel, which lets you to customize with different content, such as your pictures, bookmarks, and social feeds, sporting a 10.1 inches WXGA capacitive touch screen with 1280 x 800 pixels of resolution, equipped with 3 megapixel rear camera with LED flash and a 2 megapixel front camera, HSPA+ connectivity up to 21Mbps, 720p HD video recording capability, 1080p HD playback, DLNA support, Bluetooth 2.1, USB 2.0, gyroscope, Wi-Fi 802.11 a/b/g/n, micro-SD slot, 3.5mm headphone jack, and SIM slot, including the Samsung Stick – a Bluetooth microphone that can be carried in a pocket like a pen and sound dock with powered subwoofer.\nSamsung Galaxy Tab 10.1 will come in 16GB / 32GB / 64GB verities and pre-loaded with Social Hub, Reader’s Hub, Music Hub and Samsung Mini Apps Tray – which gives you access to more commonly used apps to help ease multitasking and it is capable of Adobe Flash Player 10.2, powered by 6860mAh battery that gives you 10hours of video-playback time. äö"""
        assert self.product_page.get_name() == 'Samsung Galaxy Tab 10.1'
        assert self.product_page.get_description() == description
        assert self.product_page.get_price() == '$241.99'
        assert self.product_page.get_ex_tax() == '$199.99'
        

    def test_add_to_cart(self):
        self.product_page.add_to_cart()
        assert  'Success: You have added' in self.product_page.get_alert_success()


    def teardown_method(self):
        if self.driver:
            self.driver.quit()