from pages.base_page import BasePage
from locators.home_locators import HomeLocators

class HomePage(BasePage):
    
    # метод ожидания появления аккардиона вопросов и нажатие на него по индексу
    def click_for_questions(self, index):
        questions = self.find_all(HomeLocators.question_element)
        element = questions[index]
        self.scroll_to(element)
        self.js_click(element)

    # получение ответа по вопросу
    def get_answer_text(self, index):
        answer = HomeLocators.answer_by_index(index)
        return self.get_text(answer)

    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        self.scroll_to(HomeLocators.order_button)
        self.click(HomeLocators.order_button)