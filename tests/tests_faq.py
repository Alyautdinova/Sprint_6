import pytest
from pages.home_page import HomePage
from data.data_test import QUESTIONS
from data.urls import Urls
from selenium.webdriver.chrome.webdriver import WebDriver

class TestFaq:

    @pytest.mark.parametrize("index", QUESTIONS.keys())
    def test_faq_1(self, driver: WebDriver, index):
        # распаковка кортежа в словаре QUESTIONS
        question, expected_answer = QUESTIONS[index]

        #открытие страницы
        driver.get(Urls.BASE_URL)

        # создание объекта страницы HomePage
        homePage = HomePage(driver)

        # нажатие во вопросу
        homePage.wait_and_click_for_questions(index)

        # сравнение ожидаемого ответа с полученным
        actual_answer = homePage.get_answer_text(index)
        assert actual_answer == expected_answer
