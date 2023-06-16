import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Urls


class BasePage:
    SCOOTER_LOGO = (By.XPATH, '//img[@src="/assets/scooter.svg"]')
    YANDEX_LOGO = (By.XPATH, '//img[@src="/assets/ya.svg"]')
    HOME_HEADER_SCOOTER_MAIN_PAGE = (By.CLASS_NAME, "Home_Header__iJKdX")
    YANDEX_PROMO_WINDOW_CLOSE_BUTTON = (By.TAG_NAME, 'svg')
    PAGE_BODY = (By.XPATH, '//div')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть главную страницу сайта')
    @allure.link(Urls.MAIN_PAGE, name='Ссылка на страницу')
    def open_site(self):
        self.driver.get(Urls.MAIN_PAGE)

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

    @allure.step('Возвращаемся на главную страницу кликом на лого Самокат')
    def click_on_scooter_logo(self):
        locator = BasePage.SCOOTER_LOGO
        return self.find_element_by_locator(locator, time=5).click()

    @allure.step('Переходим на страницу  кликом на лого Яндекс')
    def click_on_yandex_logo(self):
        locator = BasePage.YANDEX_LOGO
        return self.find_element_by_locator(locator, time=5).click()

    @allure.step('Переходим в новую открытую вкладку')
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Дожидаемся загрузки тела страницы и Получаем URL текущей страницы')
    def get_url_current_page(self, time=10):
        locator = BasePage.PAGE_BODY
        WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Не найден локатор {locator}')
        return self.driver.current_url
