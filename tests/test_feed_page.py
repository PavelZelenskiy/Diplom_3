import pytest
import allure

from ..page_objects.constructor_page import ConstructorPage
from ..page_objects.main_page import MainPage
from ..page_objects.feed_page import FeedPage

@pytest.mark.usefixtures("login_with_valid_creds")
class TestFeedPage:

    @allure.title('Проверка изменения значения счетчика: Выполнено за все время')
    @allure.description('Проверка изменения значения счетчика: Выполнено за все время')
    def test_check_all_time_counter(self, driver):
        constructor_page = ConstructorPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_feed_button()
        start_count = feed_page.get_all_time_counter()
        main_page.click_constructor_button()
        constructor_page.add_order()
        constructor_page.wait_for_modal_order_load()
        constructor_page.wait_for_load_modal_order_close_button()
        constructor_page.click_modal_order_close_button()
        main_page.wait_for_load_feed_button()
        main_page.click_feed_button()
        end_count = feed_page.get_all_time_counter()
        
        assert int(end_count) == int(start_count) + 1 

    @allure.title('Проверка изменения значения счетчика: Выполнено за сегодня')
    @allure.description('Проверка изменения значения счетчика: Выполнено за сегодня')
    def test_check_today_counter(self, driver):
        constructor_page = ConstructorPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.click_feed_button()
        start_count = feed_page.get_today_counter()
        main_page.click_constructor_button()
        constructor_page.add_order()
        constructor_page.wait_for_modal_order_load()
        constructor_page.wait_for_load_modal_order_close_button()
        constructor_page.click_modal_order_close_button()
        main_page.wait_for_load_feed_button()
        main_page.click_feed_button()
        end_count = feed_page.get_today_counter()
        
        assert int(end_count) == int(start_count) + 1 

    @allure.title('Проверка отображения номера заказа в очереди заказов')
    @allure.description('Проверка отображения номера заказа в очереди заказов')
    def test_check_order_number_in_queue(self, driver):
        constructor_page = ConstructorPage(driver)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        constructor_page.add_order()
        constructor_page.wait_for_modal_order_load()
        order_number = constructor_page.get_order_number()
        constructor_page.wait_for_load_modal_order_close_button()
        constructor_page.click_modal_order_close_button()
        main_page.wait_for_load_feed_button()
        main_page.click_feed_button()
        feed_page.wait_for_order_number_in_queue(order_number)
        order_number_in_queue = feed_page.get_in_process_order_number()
        assert '0' + order_number == order_number_in_queue

