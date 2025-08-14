import pytest
import allure

from ..page_objects.main_page import MainPage
from ..urls import *

class TestMainPage:

    @pytest.mark.usefixtures("feed_page")
    @allure.title('Проверка перехода по нажатию на элемент: кнопка "Конструктор"')
    @allure.description('Проверка перехода на вкладку "Конструктор"')
    def test_check_construction_button_transition(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_overlay_unload()
        main_page.wait_for_load_constructor_button()
        main_page.click_constructor_button()
        current_url = main_page.get_current_url()
        assert current_url == BASE_URL



    @pytest.mark.usefixtures("main_page")
    @allure.title('Проверка перехода по нажатию на элемент: кнопка "Лента Заказов"')
    @allure.description('Проверка перехода на вкладку "Лента Заказов"')
    def test_check_feed_button_transition(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_overlay_unload()
        main_page.wait_for_load_feed_button()
        main_page.click_feed_button()
        current_url = main_page.get_current_url()
        assert current_url == FEED_URL