from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):
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

    # метод заполнения поля "Имя"
    def set_first_name(self, first_name):
        self.send_keys(self.first_name_input, first_name)

    # метод заполнения поля "Фамилия"
    def set_last_name(self, last_name):
        self.send_keys(self.last_name_input, last_name)

    # метод заполнения поля "Адрес"
    def set_address(self, address):
        self.send_keys(self.address_input, address)

    # метод заполнения поля "Станция метро"
    def set_metro_station(self, metro_station):
        self.click(self.metro_station_input)
        station_option = (By.XPATH,
                            f"//div[contains(@class,'select-search__select')]"
                            f"//div[contains(@class,'Order_Text__2broi') and text()='{metro_station}']")
        self.scroll_to(station_option)
        self.click(station_option)

    # метод заполнения поля "Телефон"
    def set_phone(self, phone):
        self.send_keys(self.phone_input, phone)

    # метод нажатия на кнопку "Далее"
    def click_next_button(self):
        self.click(self.next_button)

    # метод для заказа, заполнение полей "Для кого самокат"
    def order_about_client(self, data):
        self.set_first_name(data["name"])
        self.set_last_name(data["surname"])
        self.set_address(data["address"])
        self.set_metro_station(data["metro"])
        self.set_phone(data["phone"])
        self.click_next_button()

    # метод заполнения поля "Когда привезти самокат"
    def set_bring_date(self, date):
        self.send_keys(self.bring_date_input, date)
        # закрываем календарь по клику на нейтральному месту
        self.click(self.body_name)

    # метод заполнения поля "Срок аренды"
    def set_rental_period(self, rental_period):
        self.click(self.rental_period_dropdown)
        rental_period_option = (By.XPATH,
                            f"//div[contains(@class,'Dropdown-menu')]"
                            f"//div[contains(@class,'Dropdown-option') and text()='{rental_period}']")
        self.click(rental_period_option)

    # метод для выбора цвета самоката (чёрный жемчуг или серая безысходность)
    def set_color_of_scooter(self, color_name):
        color_of_scooter_checkbox = (By.XPATH, f"//div[contains(@class,'Order_Checkboxes')]//label[text()='{color_name}']")
        self.click(color_of_scooter_checkbox)

    # метод заполнения поля "Комментарий для курьера"
    def set_comment_for_courier(self, comment):
        self.send_keys(self.comment_for_courier_input, comment)

    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        self.click(self.order_button)

    # метод для заказа, заполнение полей "Про аренду"
    def order_about_rental(self, data):
        self.set_bring_date(data["date"])
        self.set_rental_period(data["rental"])
        self.set_color_of_scooter(data["color"])
        self.set_comment_for_courier(data["comment"])
        self.click_order_button()
    