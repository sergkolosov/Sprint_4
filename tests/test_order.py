import allure

from pages.main_page import MainPageAction
from pages.order_page_first import OrderPageFirsAction
from pages.order_page_second import OrderPageSecondAction


class TestOrder:
    @allure.feature('Тестируем флоу Заказ самоката')
    @allure.story('Тесты')
    @allure.title('Проверка флоу позитивного сценария Заказ самоката через кнопку Заказать в шапке главной страницы')
    @allure.description('Проходим весь путь оформления заказа и проверяем что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_order_via_order_button_in_the_header(self, driver):
        main_page = MainPageAction(driver)
        order_page_first = OrderPageFirsAction(driver)
        order_page_second = OrderPageSecondAction(driver)

        main_page.open_site()
        main_page.click_order_button_in_the_header_page()

        order_page_first.all_field_input_and_next()
        order_page_second.all_field_input_and_next()
        actually_value = order_page_second.get_order_completed_modal_window_header_text()

        expected_value = 'Заказ оформлен'
        assert expected_value in actually_value, f'Ожидалось наличие надписи: "{expected_value}", в "{actually_value}"'

    @allure.feature('Тестируем флоу Заказ самоката')
    @allure.story('Тесты')
    @allure.title('Проверка флоу позитивного сценария Заказ самоката через кнопку Заказать в теле главной страницы')
    @allure.description('Проходим весь путь оформления заказа и проверяем что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_order_via_order_button_in_the_body(self, driver):
        main_page = MainPageAction(driver)
        order_page_first = OrderPageFirsAction(driver)
        order_page_second = OrderPageSecondAction(driver)

        main_page.open_site()
        main_page.click_order_button_in_the_body_page()

        order_page_first.all_field_input_and_next()
        order_page_second.all_field_input_and_next()
        actually_value = order_page_second.get_order_completed_modal_window_header_text()

        expected_value = 'Заказ оформлен'
        assert expected_value in actually_value, f'Ожидалось наличие надписи: "{expected_value}", в "{actually_value}"'