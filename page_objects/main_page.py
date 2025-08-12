import allure
import time

from ..locators.main_page_locators import MainPageLocators
from ..page_objects.base_page import BasePage

class MainPage(BasePage):

    #constructor tab
    @allure.step('Ожидание загрузки: кнопка "Конструктор"')    
    def wait_for_load_constructor_button(self):
        self.wait_for_element_unload(MainPageLocators.overlay)
        self.wait_for_element_to_be_clickable(MainPageLocators.constructor_button)

    @allure.step('Нажатие на элемент: кнопка "Конструктор"')
    def click_constructor_button(self):
        self.click_element(MainPageLocators.constructor_button)

    #feed tab
    @allure.step('Ожидание загрузки: кнопка "Лента Заказов"')    
    def wait_for_load_feed_button(self):
        self.wait_for_element_unload(MainPageLocators.overlay)
        self.wait_for_element_load(MainPageLocators.feed_button)

    @allure.step('Нажатие на элемент: кнопка "Лента Заказов"')
    def click_feed_button(self):
        self.click_element(MainPageLocators.feed_button)

    #overlay unload
    @allure.step('Ожидание удаления оверлей')    
    def wait_for_overlay_unload(self):
        self.wait_for_element_unload(MainPageLocators.overlay)
        

    