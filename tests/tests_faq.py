import pytest
import allure
from pages.home_page import HomePage
from data.data_test import QUESTIONS
from data.urls import Urls
from selenium.webdriver.chrome.webdriver import WebDriver

class TestFaq:

    # тест по открытию ответов на вопросы
    @allure.title('Открытие вопроса FAQ и проверка корректности ответа')
    @allure.description('Проверяем, что при клике на вопрос в разделе FAQ раскрывается правильный ответ, соответствующий этому вопросу')
    @pytest.mark.parametrize("index", QUESTIONS.keys())
    def test_faq_opens_correct_answer(self, driver: WebDriver, index):
        # распаковка кортежа в словаре QUESTIONS
        question, expected_answer = QUESTIONS[index]

        with allure.step('Открытие главной страницы'):
            driver.get(Urls.BASE_URL)

        with allure.step(f'Нажатие по вопросу №{index}: "{question}"'):
            homePage = HomePage(driver)
            homePage.click_for_questions(index)

        with allure.step('Проверка текст ответа'):
            actual_answer = homePage.get_answer_text(index)
            assert actual_answer == expected_answer
