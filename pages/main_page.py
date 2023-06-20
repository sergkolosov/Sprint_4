import allure
from selenium.webdriver.common.by import By

from data import Urls
from pages.base_page import BasePage


class MainPageLocator:
    ORDER_BUTTON_IN_THE_HEADER = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[contains(text(),"Заказать")]')
    ORDER_BUTTON_IN_THE_BODY = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[contains(text(),"Заказать")]')
    FAQ_ACCORDION_BLOCK = (By.XPATH, '//div[contains(text(),"Вопросы о важном")]')
    HOME_HEADER_BLOCK = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')
    SCOOTER_LOGO = (By.XPATH, '//img[@src="/assets/scooter.svg"]')
    YANDEX_LOGO = (By.XPATH, '//img[@src="/assets/ya.svg"]')
    PAGE_BODY_ELEMENTS = (By.XPATH, '//div')


class MainPageAction(BasePage):

    @allure.step('Открыть главную страницу сайта')
    @allure.link(Urls.MAIN_PAGE, name='Ссылка на страницу')
    def open_site(self):
        self.driver.get(Urls.MAIN_PAGE)

    @allure.step('Кликнуть кнопку "Заказать" в шапке страницы')
    def click_order_button_in_the_header_page(self):
        return self.find_element_by_locator(MainPageLocator.ORDER_BUTTON_IN_THE_HEADER).click()

    @allure.step('Скролить к кнопке "Заказать" в теле страницы')
    def scroll_to_the_button_in_body(self):
        self.scroll_to_the_element(MainPageLocator.ORDER_BUTTON_IN_THE_BODY)

    @allure.step('Кликнуть кнопку "Заказать" в теле страницы')
    def click_order_button_in_the_body_page(self):
        self.scroll_to_the_button_in_body()
        return self.find_element_by_locator(MainPageLocator.ORDER_BUTTON_IN_THE_BODY).click()

    @allure.step('Скролить к блоку FAQ')
    def scroll_to_the_accordion_block(self):
        self.scroll_to_the_element(MainPageLocator.FAQ_ACCORDION_BLOCK)

    @allure.step('Кликнуть вопрос {contains_text}')
    def click_faq_question(self, contains_text):
        locator = (By.XPATH, f'//div[contains(text(),"{contains_text}")]')
        return self.find_element_by_locator(locator).click()

    @allure.step('Получить текст ответа')
    def get_the_faq_response_text(self, contains_text):
        locator = (By.XPATH, f'//div[contains(text(),"{contains_text}")]/parent::div/parent::div/div/p')
        return self.find_element_by_locator(locator).text

    @allure.step('Найти на главной странице верхний рекламный блок')
    def find_home_header_block(self):
        return self.find_element_by_locator(MainPageLocator.HOME_HEADER_BLOCK)

    @allure.step('Возвращаемся на главную страницу кликом на лого Самокат')
    def click_on_scooter_logo(self):
        locator = MainPageLocator.SCOOTER_LOGO
        return self.find_element_by_locator(locator).click()

    @allure.step('Переходим на страницу  кликом на лого Яндекс')
    def click_on_yandex_logo(self):
        locator = MainPageLocator.YANDEX_LOGO
        return self.find_element_by_locator(locator).click()

    @allure.step('Получаем URL главной страницы Яндекс')
    def get_url_yandex_page(self):
        return self.get_url_current_page(MainPageLocator.PAGE_BODY_ELEMENTS)
