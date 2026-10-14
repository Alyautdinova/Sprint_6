import pytest
from pages.home_page import HomePage
from pages.header_page import HeaderPage
from pages.order_page import OrderPage
from data.urls import Urls
from data.data_test import ORDER_DATA_1, ORDER_DATA_2
from selenium.webdriver.chrome.webdriver import WebDriver

class TestOrder:

    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    def test_order(self, driver: WebDriver, order_data):
        
        # открытие страницы
        driver.get(Urls.BASE_URL)

        # создание объекта страницы HeaderPage
        headerPage = HeaderPage(driver)

        # нажатие на кнопку "Заказать" в хедере
        headerPage.click_order_button()

        # создание объекта страницы OrderPage
        orderPage = OrderPage(driver)

        # заполнение полей "Для кого самокат"
        orderPage.order_about_client(order_data)

        # заполнение полей "Про аренду"
        orderPage.order_about_rental(order_data)
