import pytest
import allure

from ..page_objects.constructor_page import ConstructorPage

class TestConstructorPage:

    @classmethod
    def setup_class(cls):
        cls.driver = None

    @pytest.mark.usefixtures("main_page")
    class TestIngridients:

        @allure.title('Проверка отображения модального окна "Детали ингртдиента" по нажатию на элемент: ингридиент')
        @allure.description('Проверка отображения модального окна "Детали ингртдиента" по нажатию на элемент: ингридиент')
        def test_check_modal_ingr_details_is_displayed(self):
            constructor_page = ConstructorPage(self.driver)
            constructor_page.wait_for_load_ingridient()
            constructor_page.click_ingridient()
            element = constructor_page.get_modal_ingr_details()
            assert element
            

        @allure.title('Проверка закрытия модального окна "Детали ингртдиента" по нажатию на элемент: кнопка закрыть')
        @allure.description('Проверка закрытия модального окна "Детали ингртдиента" по нажатию на элемент: кнопка закрыть')
        def test_close_modal_ingr_details(self):
            constructor_page = ConstructorPage(self.driver)
            constructor_page.wait_for_load_ingridient()
            constructor_page.click_ingridient()
            constructor_page.wait_for_load_modal_ingr_details()
            constructor_page.wait_for_load_modal_ingr_close_button()
            constructor_page.click_modal_ingr_close_button()
            element =  constructor_page.wait_for_unload_modal_ingr_details()
            assert not element
            

        @allure.title('Проверка изменения счетчика ингридиента при добавлении в заказ')
        @allure.description('Проверка изменения счетчика ингридиента при добавлении в заказ')
        def test_check_ingridient_counter(self):
            constructor_page = ConstructorPage(self.driver)
            constructor_page.wait_for_load_ingridient()
            start_count = constructor_page.get_ingridient_counter()
            constructor_page.drag_and_drop_ingridient_to_order()
            constructor_page.wait_for_load_ingridient()
            end_count = constructor_page.get_ingridient_counter()
            assert int(end_count) == int(start_count) + 2 
            