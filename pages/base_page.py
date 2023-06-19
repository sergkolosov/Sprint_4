import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу сайта {page_url}')
    def open_page(self, page_url):
        self.driver.get(page_url)

    def find_element_by_locator(self, locator, time=10):
        """Поиск с ожиданием кликабельности"""
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Не найден локатор {locator}')

    def scroll_to_the_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'Не найден локатор {locator}')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Переходим во вкладку браузера {window_number}')
    def switch_to_window_with_number(self, window_number):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Дожидаемся загрузки элемента {locator} в DOM и получаем URL текущей страницы')
    def get_url_current_page(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Не найден локатор {locator}')
        return self.driver.current_url
