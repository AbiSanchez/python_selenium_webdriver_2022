from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.login_page import LoginPage


class TestFinalLoginPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        # self.driver.get('https://laboratorio.qaminds.com/index.php?route=account/login')
        self.login_page = LoginPage(self.driver)
        self.login_page.goto('https://laboratorio.qaminds.com/index.php?route=account/login')

    def test_invalid_login(self):         # CUENTA INVALIDA
        # 1. Abrir explorador
        # 2. Ir a la URL
        # 3. Ingresar un usuario y password invalidos
        # 4. Dar clic en el boton login
        # 5. Validar que el mensaje de alarta se muestra.
        self.login_page.login('asanchez@gmail.com','password_error')
        assert self.login_page.is_login_warn_displayed(), "El mensaje no se muestra"

    def test_forgot_password(self):      #OLVIDASTE TU PASSWORD
        # 1. Abrir explorador 
        # 2. Ir a la URL
        # 3. Dar clic en el boton Forgotten Password
        self.login_page.forgotten_password()

    
    def test_menus(self):         #MENUS
        # 1. Abrir el explorador
        # 2. Ir a la URL
        # 3. Dar clic en el boton del menu REGISTER
        menu = 'Register'
        self.login_page.select_menu(menu)
                
    def teardown_method(self):
        if self.driver:
            self.driver.quit()