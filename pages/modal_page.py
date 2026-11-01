from pages.base_page import BasePage
from locators.modal_locators import ModalLocators

class ModalPage(BasePage):
    
    # метод нажатия на кнопку "Да" в модальном окне "Хотите оформить заказ?"
    def click_yes_button(self):
        self.click(ModalLocators.yes_button)

    # метод для получения текстового значения заголовка модального окна "Заказ оформлен"
    def get_order_modal_header(self):
        return self.get_text(ModalLocators.order_modal_header)
    