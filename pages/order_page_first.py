import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPageFirstLocator:
    FIRST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.CLASS_NAME, 'select-search__input')
    PHONE_NUMBER_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')


class OrderPageFirsAction(BasePage):

    @allure.step('Ввести в поле "Имя" {first_name}')
    def first_name_field_input(self, first_name):
        return self.find_element_by_locator(OrderPageFirstLocator.FIRST_NAME_FIELD, time=2).send_keys(first_name)

    @allure.step('Ввести в поле "Фамилия" {last_name}')
    def last_name_field_input(self, last_name):
        return self.find_element_by_locator(OrderPageFirstLocator.LAST_NAME_FIELD, time=2).send_keys(last_name)

    @allure.step('Ввести в поле "Адрес" {address}')
    def address_field_input(self, address):
        return self.find_element_by_locator(OrderPageFirstLocator.ADDRESS_FIELD, time=2).send_keys(address)

    @allure.step('Выбрать "Станцию метро" {metro_station}')
    def metro_station_choice(self, metro_station):
        locator = (By.XPATH, f'//div[contains(text(),"{metro_station}")]')
        self.find_element_by_locator(OrderPageFirstLocator.METRO_STATION_INPUT, time=2).click()
        return self.scroll_to_the_element(locator, time=5).click()

    @allure.step('Ввести в поле "Телефон" {phone_number}')
    def phone_number_field_input(self, phone_number):
        return self.find_element_by_locator(OrderPageFirstLocator.PHONE_NUMBER_FIELD, time=2).send_keys(phone_number)

    @allure.step('Кликнуть кнопку "Далее"')
    def click_next_button(self):
        return self.find_element_by_locator(OrderPageFirstLocator.NEXT_BUTTON, time=2).click()

    def all_field_input_and_next(self, first_name, last_name, address, metro_station, phone_number):
        self.first_name_field_input(first_name)
        self.last_name_field_input(last_name)
        self.address_field_input(address)
        self.metro_station_choice(metro_station)
        self.phone_number_field_input(phone_number)
        self.click_next_button()
