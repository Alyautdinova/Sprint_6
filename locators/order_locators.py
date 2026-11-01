from selenium.webdriver.common.by import By

class OrderLocators:
    first_name_input = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_station_input = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    phone_input= [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, "//div[contains(@class, 'Order_NextButton')]/button[text()='Далее']"]
    bring_date_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rental_period_dropdown = [By.XPATH, "//div[contains(@class,'Dropdown')][text()='* Срок аренды']"]
    comment_for_courier_input = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    order_button = [By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"]
    body_name = [By.TAG_NAME, "body"]

    @staticmethod
    def metro_option(metro_station):
        return (By.XPATH,
                    f"//div[contains(@class,'select-search__select')]"
                    f"//div[contains(@class,'Order_Text__2broi') and text()='{metro_station}']")

    @staticmethod
    def rental_option(rental_period):
        return (By.XPATH,
                    f"//div[contains(@class,'Dropdown-menu')]"
                    f"//div[contains(@class,'Dropdown-option') and text()='{rental_period}']")

    @staticmethod
    def color_option(color_name):
        return (By.XPATH, f"//div[contains(@class,'Order_Checkboxes')]//label[text()='{color_name}']")