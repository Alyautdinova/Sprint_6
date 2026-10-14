from selenium.webdriver.common.by import By

class HeaderPage:
    order_button = [By.XPATH, "//div[contains(@class,'Header')]/button[text()='Заказать']"]
    scooter_logo = [By.XPATH, "//a[contains(@class,'Header_LogoScooter')]"]
    yandex_logo = [By.XPATH, "//a[contains(@class,'Header_LogoYandex')]"]

    def __init__(self, driver):
        self.driver = driver
    
    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    # метод нажатия на логотип "Самокат"
    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()

    # метод нажатия на логотип "Яндекс"
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()
    