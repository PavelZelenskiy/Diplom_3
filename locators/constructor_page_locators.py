from selenium.webdriver.common.by import By

class ConstructorPageLocators:
    h1_header = [By.XPATH, "//h1[contains(text(), 'Соберите бургер')]"]
    modal_ingr_details_opened = [By.XPATH, '//section[contains(@class, "opened")]']
    modal_ingr_details_header = [By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]"]
    modal_ingr_details_close_button = [By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]/../../button"]
    order_button = [By.XPATH, "//button[contains(text(), 'Оформить заказ')]"]
    modal_order_number = [By.XPATH, "//p[contains(text(), 'идентификатор заказа')]/../h2"]
    modal_order_close_button = [By.XPATH, "//p[contains(text(), 'идентификатор заказа')]/../../button"]
    modal_order_loading_animation = [By.XPATH, "//img[contains(@alt, 'loading animation')]"]
    order_drop_area = [By.XPATH, "//ul[contains(@class, 'Constructor_basket')]"]

    
    def get_ingridient_locator(ingr):
        ingridient_locator = [By.XPATH, f'//p[contains(text(), "{ingr["name"]}")]']
        return ingridient_locator

    def get_ingridient_counter(ingr):
        counter_locator = [By.XPATH, f'//p[contains(text(), "{ingr["name"]}")]/..//p[contains(@class, "counter")]']
        return counter_locator