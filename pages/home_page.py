from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage

class HomePage(BasePage):
    # локатор-аккардион вопросов
    question_element = [By.XPATH , "//div[contains(@class,'accordion')]//div[contains(@class,'item')]"]
    order_button = [By.XPATH, "//div[contains(@class,'Home')]/button[text()='Заказать']"]

    # метод ожидания появления аккардиона вопросов и нажатие на него по индексу
    def click_for_questions(self, index):
        questions = self.find_all(self.question_element)
        element = questions[index]
        self.scroll_to(element)
        self.js_click(element)

    # получение ответа по вопросу
    def get_answer_text(self, index):
        answer = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, f"(//div[contains(@class,'accordion')]//div[contains(@class,'item')])[{index + 1}]//p")))
        return self.get_text(answer)

    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        self.scroll_to(self.order_button)
        self.click(self.order_button)