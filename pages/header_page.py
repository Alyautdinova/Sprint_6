from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class HeaderPage(BasePage):
    
    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        self.click(HeaderLocators.order_button)

    # метод нажатия на логотип "Самокат"
    def click_scooter_logo(self):
        self.click(HeaderLocators.scooter_logo)

    # метод нажатия на логотип "Яндекс"
    def click_yandex_logo(self):
        self.click(HeaderLocators.yandex_logo)
    