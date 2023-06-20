from random import choices, randint

import allure
from faker import Faker
from selenium.webdriver.common.by import By

from data import MetroStation, RentalPeriod, ScooterColor
from pages.base_page import BasePage


class OrderPageLocator:
    FIRST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_NUMBER_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(text(),"Далее")]')

    ABOUT_RENT_TITLE = (By.XPATH, '//div[contains(text(),"Про аренду")]')
    WHEN_TO_BRING_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    NEXT_MONTH_BUTTON_IN_CALENDAR = (By.XPATH, '//button[@aria-label="Next Month"]')
    RENTAL_PERIOD_FIELD = (By.XPATH, '//div[contains(text(),"* Срок аренды")]')
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[contains(text(),"Заказать")]')
    YES_BUTTON = (By.XPATH, '//button[contains(text(),"Да")]')
    VIEW_STATUS_BUTTON = (By.XPATH, '//button[contains(text(),"Посмотреть статус")]')
    ORDER_COMPLETED_MODAL_WINDOW_HEADER = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')


class OrderPageAction(BasePage):

    @allure.step('Ввести в поле "Имя" {first_name}')
    def first_name_field_input(self, first_name):
        return self.find_element_by_locator(OrderPageLocator.FIRST_NAME_FIELD).send_keys(first_name)

    @allure.step('Ввести в поле "Фамилия" {last_name}')
    def last_name_field_input(self, last_name):
        return self.find_element_by_locator(OrderPageLocator.LAST_NAME_FIELD).send_keys(last_name)

    @allure.step('Ввести в поле "Адрес" {address}')
    def address_field_input(self, address):
        return self.find_element_by_locator(OrderPageLocator.ADDRESS_FIELD).send_keys(address)

    @allure.step('Выбрать "Станцию метро" {metro_station}')
    def metro_station_choice(self, metro_station):
        locator = (By.XPATH, f'//div[contains(text(),"{metro_station}")]')
        self.find_element_by_locator(OrderPageLocator.METRO_STATION_INPUT).click()
        return self.scroll_to_the_element(locator).click()

    @allure.step('Ввести в поле "Телефон" {phone_number}')
    def phone_number_field_input(self, phone_number):
        return self.find_element_by_locator(OrderPageLocator.PHONE_NUMBER_FIELD).send_keys(phone_number)

    @allure.step('Кликнуть кнопку "Далее"')
    def click_next_button(self):
        return self.find_element_by_locator(OrderPageLocator.NEXT_BUTTON).click()

    def all_field_first_screen_input_and_next(self):
        fake = Faker(locale="ru_RU")
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = (fake.street_name() + ', ' + str(randint(1, 300)) + '-' + str(randint(1, 300)))
        metro_station = choices(MetroStation.metro_station)[0].get('name')
        phone_number = fake.msisdn()

        self.first_name_field_input(first_name)
        self.last_name_field_input(last_name)
        self.address_field_input(address)
        self.metro_station_choice(metro_station)
        self.phone_number_field_input(phone_number)
        self.click_next_button()

    @allure.step('Выбрать "Когда привезти самокат" {when_to_bring}')
    def when_to_bring_field_input(self, when_to_bring):
        self.find_element_by_locator(OrderPageLocator.WHEN_TO_BRING_FIELD).send_keys(when_to_bring)
        return self.find_element_by_locator(OrderPageLocator.ABOUT_RENT_TITLE).click()

    @allure.step('Выбрать "Срок аренды" {rental_period}')
    def rental_period_field_input(self, rental_period):
        locator = (By.XPATH, f'//div[contains(text(),"{rental_period}")]')
        self.find_element_by_locator(OrderPageLocator.RENTAL_PERIOD_FIELD).click()
        return self.scroll_to_the_element(locator).click()

    @allure.step('Выбрать "Цвет самоката" {scooter_color}')
    def scooter_color_checkbox_input(self, scooter_color):
        return self.find_element_by_locator((By.ID, f'{scooter_color}')).click()

    @allure.step('Ввести в поле "Комментарий" {comment}')
    def comment_field_input(self, comment):
        return self.find_element_by_locator(OrderPageLocator.COMMENT_FIELD).send_keys(comment)

    @allure.step('Кликнуть кнопку "Заказать"')
    def click_order_button(self):
        return self.find_element_by_locator(OrderPageLocator.ORDER_BUTTON).click()

    @allure.step('Кликнуть кнопку "Да"')
    def click_yes_button(self):
        return self.find_element_by_locator(OrderPageLocator.YES_BUTTON).click()

    def all_field_second_screen_input_and_next(self):
        fake = Faker(locale="ru_RU")
        when_to_bring = str(fake.future_date())
        rental_period = choices(RentalPeriod.rental_period_visible)[0]
        scooter_color = choices(ScooterColor.scooter_color)[0]
        comment = fake.sentence(nb_words=5)

        self.when_to_bring_field_input(when_to_bring)
        self.rental_period_field_input(rental_period)
        self.scooter_color_checkbox_input(scooter_color)
        self.comment_field_input(comment)
        self.click_order_button()
        self.click_yes_button()

    @allure.step('Получить текст в заголовке модального окна')
    def get_order_completed_modal_window_header_text(self):
        return self.find_element_by_locator(OrderPageLocator.ORDER_COMPLETED_MODAL_WINDOW_HEADER).text

