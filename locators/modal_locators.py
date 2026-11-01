from selenium.webdriver.common.by import By

class ModalLocators:
    yes_button = [By.XPATH, "//button[text()='Да']"]
    order_modal_header = [By.XPATH, "//div[contains(@class,'Order_ModalHeader')]"]