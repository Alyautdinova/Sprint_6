from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HeaderPage(BasePage):
    order_button = [By.XPATH, "//div[contains(@class,'Header')]/button[text()='Заказать']"]
    scooter_logo = [By.XPATH, "//a[contains(@class,'Header_LogoScooter')]"]
    yandex_logo = [By.XPATH, "//a[contains(@class,'Header_LogoYandex')]"]

    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        self.click(self.order_button)

    # метод нажатия на логотип "Самокат"
    def click_scooter_logo(self):
        self.click(self.scooter_logo)

    # метод нажатия на логотип "Яндекс"
    def click_yandex_logo(self):
        self.click(self.yandex_logo)
    