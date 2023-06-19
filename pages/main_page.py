import allure
from selenium.webdriver.common.by import By

from data import Urls
from pages.base_page import BasePage


class MainPageLocator:
    ORDER_BUTTON_IN_THE_HEADER = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    ORDER_BUTTON_IN_THE_BODY_BLOCK = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]')
    ORDER_BUTTON_IN_THE_BODY = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')
    FAQ_ACCORDION_BLOCK = (By.XPATH, '//div[@class="accordion"]')
    HOME_HEADER_BLOCK = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')


class MainPageAction(BasePage):

    @allure.step('Открыть главную страницу сайта')
    @allure.link(Urls.MAIN_PAGE, name='Ссылка на страницу')
    def open_site(self):
        self.driver.get(Urls.MAIN_PAGE)

    @allure.step('Кликнуть кнопку "Заказать" в шапке страницы')
    def click_order_button_in_the_header_page(self):
        return self.find_element_by_locator(MainPageLocator.ORDER_BUTTON_IN_THE_HEADER, time=2).click()

    @allure.step('Скролить к кнопке "Заказать" в теле страницы')
    def scroll_to_the_button_in_body(self):
        self.scroll_to_the_element(MainPageLocator.ORDER_BUTTON_IN_THE_BODY, time=5)

    @allure.step('Кликнуть кнопку "Заказать" в теле страницы')
    def click_order_button_in_the_body_page(self):
        self.scroll_to_the_button_in_body()
        return self.find_element_by_locator(MainPageLocator.ORDER_BUTTON_IN_THE_BODY, time=5).click()

    @allure.step('Скролить к блоку FAQ')
    def scroll_to_the_accordion_block(self):
        self.scroll_to_the_element(MainPageLocator.FAQ_ACCORDION_BLOCK, time=5)

    @allure.step('Кликнуть вопрос {contains_text}')
    def click_faq_question(self, contains_text):
        locator = (By.XPATH, f'//div[contains(text(),"{contains_text}")]')
        return self.find_element_by_locator(locator, time=5).click()

    @allure.step('Получить текст ответа')
    def get_the_faq_response_text(self, contains_text):
        locator = (By.XPATH, f'//div[contains(text(),"{contains_text}")]/parent::div/parent::div/div/p')
        return self.find_element_by_locator(locator, time=5).text

    @allure.step('Найти на главной странице верхний рекламный блок')
    def find_home_header_block(self):
        return self.find_element_by_locator(MainPageLocator.HOME_HEADER_BLOCK, time=5)
