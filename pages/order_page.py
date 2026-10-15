from pages.base_page import BasePage
from locators.order_locators import OrderLocators

class OrderPage(BasePage):
    
    # метод заполнения поля "Имя"
    def set_first_name(self, first_name):
        self.send_keys(OrderLocators.first_name_input, first_name)

    # метод заполнения поля "Фамилия"
    def set_last_name(self, last_name):
        self.send_keys(OrderLocators.last_name_input, last_name)

    # метод заполнения поля "Адрес"
    def set_address(self, address):
        self.send_keys(OrderLocators.address_input, address)

    # метод заполнения поля "Станция метро"
    def set_metro_station(self, metro_station):
        self.click(OrderLocators.metro_station_input)
        metro_option = OrderLocators.metro_option(metro_station)
        self.scroll_to(metro_option)
        self.click(metro_option)

    # метод заполнения поля "Телефон"
    def set_phone(self, phone):
        self.send_keys(OrderLocators.phone_input, phone)

    # метод нажатия на кнопку "Далее"
    def click_next_button(self):
        self.click(OrderLocators.next_button)

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
        self.send_keys(OrderLocators.bring_date_input, date)
        # закрываем календарь по клику на нейтральному месту
        self.click(OrderLocators.body_name)

    # метод заполнения поля "Срок аренды"
    def set_rental_period(self, rental_period):
        self.click(OrderLocators.rental_period_dropdown)
        rental_option = OrderLocators.rental_option(rental_period)
        self.click(rental_option)

    # метод для выбора цвета самоката (чёрный жемчуг или серая безысходность)
    def set_color_of_scooter(self, color_name):
        color_of_scooter_checkbox = OrderLocators.color_option(color_name)
        self.click(color_of_scooter_checkbox)

    # метод заполнения поля "Комментарий для курьера"
    def set_comment_for_courier(self, comment):
        self.send_keys(OrderLocators.comment_for_courier_input, comment)

    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        self.click(OrderLocators.order_button)

    # метод для заказа, заполнение полей "Про аренду"
    def order_about_rental(self, data):
        self.set_bring_date(data["date"])
        self.set_rental_period(data["rental"])
        self.set_color_of_scooter(data["color"])
        self.set_comment_for_courier(data["comment"])
        self.click_order_button()
    