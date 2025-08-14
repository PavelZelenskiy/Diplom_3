import allure

from ..locators.feed_page_locators import FeedPageLocators
from ..locators.constructor_page_locators import ConstructorPageLocators
from ..page_objects.base_page import BasePage
from ..page_objects.constructor_page import ConstructorPage
from ..page_objects.main_page import MainPage

class FeedPage(BasePage):

    #all time counter
    @allure.step('Получение значения счетчика: Выполнено за все время')
    def get_all_time_counter(self):
        return self.get_element_text(FeedPageLocators.all_time_counter)

    #today counter
    @allure.step('Получение значения счетчика: Выполнено за все время')
    def get_today_counter(self):
        return self.get_element_text(FeedPageLocators.today_counter)
    
    #in process order number
    @allure.step('Получение значения элемента: В работе')
    def get_in_process_order_number(self):
        return self.get_element_text(FeedPageLocators.in_process_orders)
    
    @allure.step('Ожидание появления заказа в очереди')
    def wait_for_order_number_in_queue(self, order_number):
        self.wait_for_element_text_update(FeedPageLocators.in_process_orders, order_number)