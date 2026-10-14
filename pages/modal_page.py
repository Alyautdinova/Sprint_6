from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ModalPage:
    yes_button = [By.XPATH, "//button[text()='Да']"]
    order_modal_header = [By.XPATH, "//div[contains(@class,'Order_ModalHeader')]"]

    def __init__(self, driver):
        self.driver = driver
    
    # метод нажатия на кнопку "Да" в модальном окне "Хотите оформить заказ?"
    def click_yes_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.yes_button)).click()

    # метод для получения текстового значения заголовка модального окна "Заказ оформлен"
    def get_order_modal_header(self):
        return self.driver.find_element(*self.order_modal_header).text
    