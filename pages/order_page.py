from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class OrderPage:
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


    def __init__(self, driver):
        self.driver = driver

    # метод заполнения поля "Имя"
    def set_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    # метод заполнения поля "Фамилия"
    def set_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    # метод заполнения поля "Адрес"
    def set_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    # метод заполнения поля "Станция метро"
    def set_metro_station(self, metro_station):
        self.driver.find_element(*self.metro_station_input).click()
        station_option = (By.XPATH,
                            f"//div[contains(@class,'select-search__select')]"
                            f"//div[contains(@class,'Order_Text__2broi') and text()='{metro_station}']")
        station_option_visible = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(station_option))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", station_option_visible)
        station_option_visible.click()

    # метод заполнения поля "Телефон"
    def set_phone(self, phone):
        self.driver.find_element(*self.phone_input).send_keys(phone)

    # метод нажатия на кнопку "Далее"
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

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
        self.driver.find_element(*self.bring_date_input).send_keys(date)
        # закрываем календарь по клику на нейтральному месту
        self.driver.find_element(By.TAG_NAME, "body").click()

    # метод заполнения поля "Срок аренды"
    def set_rental_period(self, rental_period):
        self.driver.find_element(*self.rental_period_dropdown).click()
        rental_period_option = (By.XPATH,
                            f"//div[contains(@class,'Dropdown-menu')]"
                            f"//div[contains(@class,'Dropdown-option') and text()='{rental_period}']")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(rental_period_option)).click()

    # метод для выбора цвета самоката (чёрный жемчуг или серая безысходность)
    def set_color_of_scooter(self, color_name):
        color_of_scooter_checkbox = (By.XPATH, f"//div[contains(@class,'Order_Checkboxes')]//label[text()='{color_name}']")
        self.driver.find_element(*color_of_scooter_checkbox).click()

    # метод заполнения поля "Комментарий для курьера"
    def set_comment_for_courier(self, comment):
        self.driver.find_element(*self.comment_for_courier_input).send_keys(comment)

    # метод нажатия на кнопку "Заказать"
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    # метод для заказа, заполнение полей "Про аренду"
    def order_about_rental(self, data):
        self.set_bring_date(data["date"])
        self.set_rental_period(data["rental"])
        self.set_color_of_scooter(data["color"])
        self.set_comment_for_courier(data["comment"])
        self.click_order_button()
    