from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage:
    # локатор-аккардион вопросов
    question_element = [By.XPATH , "//div[contains(@class,'accordion')]//div[contains(@class,'item')]"]
    order_button = [By.XPATH, "//div[contains(@class,'Home')]/button[text()='Заказать']"]

    def __init__(self, driver):
        self.driver = driver

    # метод ожидания появления аккардиона вопросов и нажатие на него по индексу
    def click_for_questions(self, index):
        questions = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(self.question_element))
        element = questions[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    # получение ответа по вопросу
    def get_answer_text(self, index):
        answer = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, f"(//div[contains(@class,'accordion')]//div[contains(@class,'item')])[{index + 1}]//p")))
        return answer.text

    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        order_button = self.driver.find_element(*self.order_button)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", order_button)
        order_button.click()