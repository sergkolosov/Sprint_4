import allure

from data import Urls, TextContentMinePage
from pages.base_page import BasePage
from pages.main_page import MainPageAction


class TestSwitch:
    @allure.feature('Тестируем переходы между страницами')
    @allure.story('Тесты')
    @allure.title('Проверка перехода на главную страницу сервиса по клику в лого Самокат')
    @allure.description('Открываем стенд на странице оформления заказа, кликаем в лого, проверяем что вернулись на главную исследуя текст верхнего рекламного блока')
    def test_order_via_order_button_in_the_header(self, driver):
        base_page = BasePage(driver)
        main_page = MainPageAction(driver)

        base_page.open_page(Urls.ORDER_PAGE)
        base_page.click_on_scooter_logo()

        actually_value = main_page.find_home_header_block().text
        expected_value_1 = TextContentMinePage.home_header_block[0]
        expected_value_2 = TextContentMinePage.home_header_block[1]

        assert expected_value_1 and expected_value_2 in actually_value, f'Ожидалось что строки: "{expected_value_1}" и "{expected_value_2}" содержатся в рекламном блоке "{actually_value}"'

    @allure.feature('Тестируем переходы между страницами')
    @allure.story('Тесты')
    @allure.title('Проверка перехода на главную страницу Яндекс по клику в лого Яндекс')
    @allure.description('Открываем стенд на главной странице, кликаем в лого, проверяем URL')
    def test_go_to_yandex_page_by_click__logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_page(Urls.MAIN_PAGE)

        base_page.click_on_yandex_logo()
        base_page.switch_to_window_with_number(1)

        actually_url = base_page.get_url_current_page()
        expected_url = Urls.YANDEX_PAGE
        assert actually_url == expected_url, f'Ожидался URL: "{expected_url}", получен "{actually_url}"'
