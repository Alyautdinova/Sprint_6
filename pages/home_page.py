from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage:
    # локатор-аккардион вопросов
    question_element = [By.XPATH , "//div[contains(@class,'accordion')]//div[contains(@class,'item')]"]

    def __init__(self, driver):
        self.driver = driver

    # метод ожидания появления аккардиона вопросов и нажатие на него по индексу
    def wait_and_click_for_questions(self, index):
        questions = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_all_elements_located(self.question_element))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", questions[index])
        questions[index].click()

    # получение ответа по вопросу
    def get_answer_text(self, index):
        answer = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, f"(//div[contains(@class,'accordion')]//div[contains(@class,'item')])[{index + 1}]//p")))
        return answer.text
    