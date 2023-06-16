import allure
from faker import Faker
from random import choices, randint

from pages.main_page import MainPageAction
from pages.order_page_first import OrderPageFirsAction
from pages.order_page_second import OrderPageSecondAction
from pages.status_page import StatusPageAction
from data import MetroStation
from data import RentalPeriod
from data import ScooterColor


class TestOrder:
    @allure.feature('Тестируем флоу Заказ самоката')
    @allure.story('Тесты')
    @allure.title('Проверка флоу позитивного сценария Заказ самоката через кнопку Заказать в шапке главной страницы')
    @allure.description('Проходим весь путь оформления заказа и проверяем что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_order_via_order_button_in_the_header(self, driver):
        main_page = MainPageAction(driver)
        order_page_first = OrderPageFirsAction(driver)
        order_page_second = OrderPageSecondAction(driver)

        fake = Faker(locale="ru_RU")
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = (fake.street_name() + ', ' + str(randint(1, 300)) + '-' + str(randint(1, 300)))
        phone_number = fake.msisdn()
        when_to_bring = str(fake.future_date())
        comment = fake.sentence(nb_words=5)

        metro_station = choices(MetroStation.metro_station)[0].get('name')
        rental_period = choices(RentalPeriod.rental_period_visible)[0]
        scooter_color = choices(ScooterColor.scooter_color)[0]

        main_page.open_site()
        main_page.click_order_button_in_the_header_page()

        order_page_first.all_field_input_and_next(first_name, last_name, address, metro_station, phone_number)
        order_page_second.all_field_input_and_next(when_to_bring, rental_period, scooter_color, comment)
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

        fake = Faker(locale="ru_RU")
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = (fake.street_name() + ', ' + str(randint(1, 300)) + '-' + str(randint(1, 300)))
        phone_number = fake.msisdn()
        when_to_bring = str(fake.future_date())
        comment = fake.sentence(nb_words=5)

        metro_station = choices(MetroStation.metro_station)[0].get('name')
        rental_period = choices(RentalPeriod.rental_period_visible)[0]
        scooter_color = choices(ScooterColor.scooter_color)[0]

        main_page.open_site()
        main_page.click_order_button_in_the_body_page()

        order_page_first.all_field_input_and_next(first_name, last_name, address, metro_station, phone_number)
        order_page_second.all_field_input_and_next(when_to_bring, rental_period, scooter_color, comment)
        actually_value = order_page_second.get_order_completed_modal_window_header_text()

        expected_value = 'Заказ оформлен'
        assert expected_value in actually_value, f'Ожидалось наличие надписи: "{expected_value}", в "{actually_value}"'