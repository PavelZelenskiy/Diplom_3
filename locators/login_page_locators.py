from selenium.webdriver.common.by import By

class LoginPageLocators:
    
    login_input = [By.NAME, 'name']
    pasword_input = [By.NAME, 'Пароль']
    login_button = [By.XPATH, "//button[contains(text(), 'Войти')]"]
    