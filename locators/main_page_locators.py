from selenium.webdriver.common.by import By

class MainPageLocators:
    constructor_button = [By.XPATH, "//p[contains(text(), 'Конструктор')]"]
    feed_button = [By.XPATH, "//p[contains(text(), 'Лента Заказов')]"]
    overlay = [By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]"]