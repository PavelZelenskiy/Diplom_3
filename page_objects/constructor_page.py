import allure
from seletools.actions import drag_and_drop

from ..locators.constructor_page_locators import ConstructorPageLocators
from ..locators.main_page_locators import MainPageLocators
from ..page_objects.base_page import BasePage
from ..data.ingridients import Ingridient

class ConstructorPage(BasePage):

    #ingridients
    @allure.step('Ожидание загрузки: ингридиент')    
    def wait_for_load_ingridient(self):
        self.wait_for_element_unload(MainPageLocators.overlay)
        ingr = ConstructorPageLocators.get_ingridient_locator(Ingridient.fluerescent_bun)
        self.wait_for_element_load(ingr)

    @allure.step('Нажатие на элемент: ингридиент')
    def click_ingridient(self):
        ingr = ConstructorPageLocators.get_ingridient_locator(Ingridient.fluerescent_bun)
        self.click_element(ingr)

    @allure.step('Получение значения счетчика: ингридиент')
    def get_ingridient_counter(self):
        return self.get_element_text(ConstructorPageLocators.get_ingridient_counter(Ingridient.fluerescent_bun))

    #modal ingridient details
    @allure.step('Ожидание загрузки: модальное окно "Детали ингридиента"')    
    def wait_for_load_modal_ingr_details(self):
        modal = ConstructorPageLocators.modal_ingr_details_opened
        self.wait_for_element_load(modal) 

    @allure.step('Ожидание удаления из DOM-дерева: модальное окно "Детали ингридиента"')
    def wait_for_unload_modal_ingr_details(self):
        modal = ConstructorPageLocators.modal_ingr_details_opened
        self.wait_for_element_unload(modal) 

    @allure.step('Получение элемента: модальное окно "Детали ингридиента"')    
    def get_modal_ingr_details(self):
        modal = ConstructorPageLocators.modal_ingr_details_opened
        return self.get_element(modal)   

    @allure.step('Получение элемента: заголовок модального окна "Детали ингридиента"')    
    def get_modal_ingr_details_header(self):
        header = ConstructorPageLocators.modal_ingr_details_header
        return self.get_element(header)
    
    @allure.step('Ожидание загрузки элемента: кнопка "Закрыть"(крестик) модального окна "Детали ингридиента"')
    def wait_for_load_modal_ingr_close_button(self):
        button = ConstructorPageLocators.modal_ingr_details_close_button
        self.wait_for_element_load(button)

    @allure.step('Нажатие на элемент: кнопка "Закрыть"(крестик) модального окна "Детали ингридиента"')
    def click_modal_ingr_close_button(self):
        button = ConstructorPageLocators.modal_ingr_details_close_button
        self.click_element(button)

    #order button
    @allure.step('Нажатие на элемент: кнопка "Оформить заказ"')
    def click_order_button(self):
        button = ConstructorPageLocators.order_button
        self.click_element(button)

    @allure.step('Ожидание загрузки элемента: кнопка "Оформить заказ"')
    def wait_for_load_order_button(self):
        button = ConstructorPageLocators.order_button
        self.wait_for_element_load(button)

    #drag n drop ingridient to order
    @allure.step('Добавление ингридиента в заказ')
    def drag_and_drop_ingridient_to_order(self):
        source = self.get_element(ConstructorPageLocators.get_ingridient_locator(Ingridient.fluerescent_bun))
        target = self.get_element(ConstructorPageLocators.order_drop_area)

        drag_and_drop(self.driver, source, target)
        
    #modal order
    @allure.step('Получение элемента: номер заказа')    
    def get_order_number(self):
        return self.get_element_text(ConstructorPageLocators.modal_order_number)
    
    @allure.step('Нажатие на элемент: кнопка "Закрыть"(крестик) модального окна заказа')
    def click_modal_order_close_button(self):
        self.click_element(ConstructorPageLocators.modal_order_close_button)

    @allure.step('Ожидание загрузки элемента: кнопка "Закрыть"(крестик) модального окна заказа')
    def wait_for_load_modal_order_close_button(self):
        button = ConstructorPageLocators.modal_order_close_button
        self.wait_for_element_load(button)
        self.wait_for_element_to_be_clickable(button)

    @allure.step('Ожидание загрузки модального окна заказа')
    def wait_for_modal_order_load(self):
        self.wait_for_element_unload(ConstructorPageLocators.modal_order_loading_animation)

    #add order
    @allure.step('Создание заказа')
    def add_order(self):
        button = ConstructorPageLocators.order_button
        self.drag_and_drop_ingridient_to_order()
        self.click_element(button)