from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ModalPage(BasePage):
    yes_button = [By.XPATH, "//button[text()='Да']"]
    order_modal_header = [By.XPATH, "//div[contains(@class,'Order_ModalHeader')]"]

    # метод нажатия на кнопку "Да" в модальном окне "Хотите оформить заказ?"
    def click_yes_button(self):
        self.click(self.yes_button)

    # метод для получения текстового значения заголовка модального окна "Заказ оформлен"
    def get_order_modal_header(self):
        return self.get_text(self.order_modal_header)
    