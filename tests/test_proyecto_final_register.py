from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.register_page import RegisterPage



class TestFinalRegisterPage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.register_page = RegisterPage(self.driver)
        self.register_page.goto("https://laboratorio.qaminds.com/index.php?route=account/register")
        
        
    def test_new_user(self):
        """STEPS :
        1. Abrir el explorador
        2. Ir a la URL
        3. Llenar los campos obligatorios.
        4. Seleccionar el check "Privacy Policy"
        5. Dar clic en el botón "Continuar"
        6. Validar que se muestra el mensaje 'Your Account Has Been Created!'"""
        first_name = 'Rosalia'
        last_name = 'Cristofono'
        email = 'rosa38@mail.com'
        telephone = '5646235689'
        password = 'Prueba01'
        psw_confirm = 'Prueba01'
        self.register_page.fill_data_user(first_name,last_name,email,telephone,password,psw_confirm)
        self.register_page.select_check_policy()
        self.register_page.select_continuar_btn()
        assert self.register_page.message_account_created() == 'Your Account Has Been Created!'



        
    def test_privacy_policy(self):
        """STEPS :
        1. Abrir el explorador
        2. Ir a la URL
        3. Llenar los campos obligatorios.
        4. NO seleccionar el check "Privacy Policy"
        5. Dar clic en el botón "Continuar"
        6. Validar que se muestra el mensaje de alerta en la parte superior del formulario."""
        first_name = 'Abigail'
        last_name = 'Lopez'
        email = 'abil@mail.com'
        telephone = '5646235689'
        password = 'Prueba01'
        psw_confirm = 'Prueba01'
        self.register_page.fill_data_user(first_name,last_name,email,telephone,password,psw_confirm)
        self.register_page.select_continuar_btn()
        self.register_page.message_policy_missing() == 'Warning: You must agree to the Privacy Policy!'
        
 
    def test_information_failed(self):
        """STEPS :
        1. Abrir el explorador
        2. Ir a la URL
        3. Llenar los campos obligatorios, excpto el campo de email.
        4. Seleccionar el check "Privacy Policy"
        5. Dar clic en el botón "Continuar"
        6. Validar que se muestra el mensaje de alterta debajo del campo email"""
        first_name = 'Abigail'
        last_name = 'Cruz'
        email = ' '
        telephone = '5646235689'
        password = 'Prueba01'
        psw_confirm = 'Prueba01'
        self.register_page.fill_data_user(first_name,last_name,email,telephone,password,psw_confirm)
        self.register_page.select_check_policy()
        self.register_page.select_continuar_btn()
        assert self.register_page.alert_email_missing() == 'E-Mail Address does not appear to be valid!'
                 

    def teardown_method(self):
        if self.driver:
            self.driver.quit()