from selenium.webdriver.common.by import By

class HomeLocators:
    question_element = [By.XPATH , "//div[contains(@class,'accordion')]//div[contains(@class,'item')]"]
    order_button = [By.XPATH, "//div[contains(@class,'Home')]/button[text()='Заказать']"]

    @staticmethod
    def answer_by_index(index):
        return (By.XPATH, f"(//div[contains(@class,'accordion')]//div[contains(@class,'item')])[{index + 1}]//p")
