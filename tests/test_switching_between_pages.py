import allure

from data import Urls
from pages.base_page import BasePage


class TestSwitch:
    @allure.feature('Тестируем переходы между страницами')
    @allure.story('Тесты')
    @allure.title('Проверка перехода на главную страницу сервиса по клику в лого Самокат')
    @allure.description('Открываем стенд на странице оформления заказа, кликаем в лого, проверяем URL')
    def test_order_via_order_button_in_the_header(self, driver):
        base_page = BasePage(driver)

        base_page.open_page(Urls.ORDER_PAGE)
        base_page.click_on_scooter_logo()

        actually_url = base_page.get_url_current_page()
        expected_url = Urls.MAIN_PAGE
        assert actually_url == expected_url, f'Ожидался URL: "{expected_url}", получен "{actually_url}"'

    @allure.feature('Тестируем переходы между страницами')
    @allure.story('Тесты')
    @allure.title('Проверка перехода на главную страницу Яндекс по клику в лого Яндекс')
    @allure.description('Открываем стенд на главной странице, кликаем в лого, проверяем URL')
    def test_go_to_yandex_page_by_click__logo(self, driver):
        base_page = BasePage(driver)
        base_page.open_site()

        base_page.click_on_yandex_logo()
        base_page.switch_to_new_window()

        actually_url = base_page.get_url_current_page()
        expected_url = Urls.YANDEX_PAGE
        assert actually_url == expected_url, f'Ожидался URL: "{expected_url}", получен "{actually_url}"'
