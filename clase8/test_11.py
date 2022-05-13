from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver




driver: WebDriver = None


def setup():
    global driver
    driver = get_driver()



def test_tablets():
    driver.get("https://laboratorio.qaminds.com/")
    header = driver.find_element(By.LINK_TEXT, 'Tablets')
    header.click()
    galaxy = driver.find_element(By.PARTIAL_LINK_TEXT, 'Samsung')
    assert galaxy.is_displayed(), 'Galaxy not found'


def test_iphone():
    driver.get("https://laboratorio.qaminds.com/")
    header = driver.find_element(By.PARTIAL_LINK_TEXT, 'Phones')
    header.click()
    iphone = driver.find_element(By.LINK_TEXT, 'iPhone')
    assert iphone.is_displayed(), 'Iphone not found'


def test_windows():
    driver.get("https://laboratorio.qaminds.com/")
    header = driver.find_element(By.PARTIAL_LINK_TEXT, 'Laptops')
    header.click()
    sub_header = driver.find_element(By.PARTIAL_LINK_TEXT, 'Windows')
    sub_header.click()
    windows = driver.find_element(By.XPATH, "//*[@id='content']/p")
    assert windows.text == 'There are no products to list in this category.', 'Products were found'


def teardown():
    if driver:
        driver.quit()