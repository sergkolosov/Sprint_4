import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPageSecondLocator:
    ABOUT_RENT_TITLE = (By.XPATH, '//div[@class="Order_Header__BZXOb"]')
    WHEN_TO_BRING_FIELD = (By.XPATH, '//div[@class="react-datepicker__input-container"]/input')
    NEXT_MONTH_BUTTON_IN_CALENDAR = (By.XPATH, '//button[@aria-label="Next Month"]')
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-control')
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    NEXT_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    YES_BUTTON = (By.XPATH, '//button[contains(text(),"Да")]')
    VIEW_STATUS_BUTTON = (By.XPATH, '//button[contains(text(),"Посмотреть статус")]')
    ORDER_COMPLETED_MODAL_WINDOW_HEADER = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')


class OrderPageSecondAction(BasePage):
    @allure.step('Выбрать "Когда привезти самокат" {when_to_bring}')
    def when_to_bring_field_input(self, when_to_bring):
        self.find_element_by_locator(OrderPageSecondLocator.WHEN_TO_BRING_FIELD, time=2).send_keys(when_to_bring)
        return self.find_element_by_locator(OrderPageSecondLocator.ABOUT_RENT_TITLE, time=2).click()

    @allure.step('Выбрать "Срок аренды" {rental_period}')
    def rental_period_field_input(self, rental_period):
        locator = (By.XPATH, f'//div[contains(text(),"{rental_period}")]')
        self.find_element_by_locator(OrderPageSecondLocator.RENTAL_PERIOD_FIELD, time=2).click()
        return self.scroll_to_the_element(locator, time=2).click()

    @allure.step('Выбрать "Цвет самоката" {scooter_color}')
    def scooter_color_checkbox_input(self, scooter_color):
        return self.find_element_by_locator((By.ID, f'{scooter_color}'), time=2).click()

    @allure.step('Ввести в поле "Комментарий" {comment}')
    def comment_field_input(self, comment):
        return self.find_element_by_locator(OrderPageSecondLocator.COMMENT_FIELD, time=2).send_keys(comment)

    @allure.step('Кликнуть кнопку "Далее"')
    def click_next_button(self):
        return self.find_element_by_locator(OrderPageSecondLocator.NEXT_BUTTON, time=2).click()

    @allure.step('Кликнуть кнопку "Да"')
    def click_yes_button(self):
        return self.find_element_by_locator(OrderPageSecondLocator.YES_BUTTON, time=2).click()

    def all_field_input_and_next(self, when_to_bring, rental_period, scooter_color, comment):
        self.when_to_bring_field_input(when_to_bring)
        self.rental_period_field_input(rental_period)
        self.scooter_color_checkbox_input(scooter_color)
        self.comment_field_input(comment)
        self.click_next_button()
        self.click_yes_button()

    @allure.step('Получить текст в заголовке модального окна')
    def get_order_completed_modal_window_header_text(self):
        return self.find_element_by_locator(OrderPageSecondLocator.ORDER_COMPLETED_MODAL_WINDOW_HEADER, time=2).text

    @allure.step('Кликнуть кнопку "Посмотреть статус"')
    def click_view_status_button(self):
        return self.find_element_by_locator(OrderPageSecondLocator.VIEW_STATUS_BUTTON, time=2).click()
