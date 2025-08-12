import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .urls import *
from .data.creds import Creds
from .page_objects.login_page import LoginPage
from .page_objects.constructor_page import ConstructorPage


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
   
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    try:
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
    finally:
        driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    driver.get(BASE_URL)
    

@pytest.fixture(scope='function')
def feed_page(driver):
    driver.get(FEED_URL)

@pytest.fixture(scope="function")
def login_with_valid_creds(request, driver):
    
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.wait_for_load_login_page()
    login_page.login(Creds.valid_user['login'], Creds.valid_user['password'])
    constructor_page = ConstructorPage(driver)
    constructor_page.wait_for_load_order_button()
    