import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StatusPageLocator:
    CANCEL_ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]')


class StatusPageAction(BasePage):
    @allure.step('Получить текст на кнопке "Отменить заказ"')
    def get_cancel_order_button_text(self):
        return self.find_element_by_locator(StatusPageLocator.CANCEL_ORDER_BUTTON, time=2).text
