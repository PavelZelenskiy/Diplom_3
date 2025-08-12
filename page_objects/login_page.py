import allure

from ..locators.login_page_locators import LoginPageLocators
from ..locators.main_page_locators import MainPageLocators
from ..page_objects.base_page import BasePage

class LoginPage(BasePage):

    @allure.step('Ожидание загрузки страницы входа в систему')
    def wait_for_load_login_page(self):
        self.wait_for_element_unload(MainPageLocators.overlay)
        self.wait_for_element_load(LoginPageLocators.login_button)

    #login input
    @allure.step('Заполнение поля "Логин"')
    def set_login(self, login):
        self.send_keys(LoginPageLocators.login_input, login)


    #password input
    @allure.step('Заполнение поля "Пароль"')
    def set_password(self, password):
        self.send_keys(LoginPageLocators.pasword_input, password)

    #login button
    @allure.step('Нажатие на кнопку "Войти"')
    def click_login_button(self):
        self.click_element(LoginPageLocators.login_button)

    #login
    @allure.step('Выполнение входа в систему')
    def login(self, login, password):
        self.set_login(login)
        self.set_password(password)
        self.click_login_button()