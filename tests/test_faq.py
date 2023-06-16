import allure

from pages.main_page import MainPageAction
from data import Faq

pytestmark = Faq.pytestmark


class TestFaq:

    @allure.feature('Тестируем соответствие вопрос-ответ в разделе «Вопросы о важном»')
    @allure.story('Тесты')
    @allure.title('Проверка вопроса {question_text}')
    @allure.description('На странице ищем элемент с вопросом, раскрываем и проверяем, что ответ соответствует вопросу')
    @allure.testcase('ссылка на тест-кейс', 'No')
    @allure.issue('ссылка на баг', 'No')
    def test_faq_question(self, driver, question_text, expected_response_text):
        main_page = MainPageAction(driver)
        main_page.open_site()
        main_page.scroll_to_the_accordion_block()
        main_page.click_faq_question(question_text)
        actually_response_text = main_page.get_the_faq_response_text(question_text)
        assert actually_response_text == expected_response_text, f'На вопрос "{question_text}" ожидался ответ: "{expected_response_text}", получено "{actually_response_text}"'
