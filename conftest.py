import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@allure.step('Открыть браузер Firefox c размерами окна 1200х600')
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size-1200,600")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
