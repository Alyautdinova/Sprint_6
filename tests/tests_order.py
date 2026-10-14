import pytest
from pages.home_page import HomePage
from pages.header_page import HeaderPage
from pages.order_page import OrderPage
from pages.modal_page import ModalPage
from pages.base_page import BasePage
from data.urls import Urls
from data.data_test import ORDER_DATA_1, ORDER_DATA_2
from selenium.webdriver.chrome.webdriver import WebDriver

class TestOrder:

    # параметризированный тест с нажатием на кнопку "Заказать" в хедере
    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    def test_scooter_order(self, driver: WebDriver, order_data):
        
        # открытие страницы
        driver.get(Urls.BASE_URL)

        # создание объекта страницы HeaderPage
        headerPage = HeaderPage(driver)

        # нажатие на кнопку "Заказать" в хедере
        headerPage.click_order_button()

        # проверка, что находимся на урле заказа самоката
        assert driver.current_url == Urls.ORDER_URL

        # создание объекта страницы OrderPage
        orderPage = OrderPage(driver)

        # заполнение полей "Для кого самокат"
        orderPage.order_about_client(order_data)

        # заполнение полей "Про аренду"
        orderPage.order_about_rental(order_data)

        # создание объекта страницы ModalPage
        modalPage = ModalPage(driver)

        # нажатие на кнопку "Да"
        modalPage.click_yes_button()

        # получение заголовка модального окна "Заказ оформлен"
        order_modal_header = modalPage.get_order_modal_header()

        # проверка заголовка модального окна "Заказ оформлен"
        assert 'Заказ оформлен' in order_modal_header

    # тест на нажатие на логотип Самокат на странице заказа самоката
    def test_click_logo_scooter(self, driver: WebDriver):

        # открытие страницы
        driver.get(Urls.BASE_URL)

        # создание объекта страницы HomePage
        homePage = HomePage(driver)

        # нажатие на кнопку "Заказать" на главной странице
        homePage.click_order_button()

        # проверка, что находимся на урле заказа самоката
        assert driver.current_url == Urls.ORDER_URL

        # создание объекта страницы HeaderPage
        headerPage = HeaderPage(driver)

        # нажатие на логотип "Скутер"
        headerPage.click_scooter_logo()

        # проверка, что находимся на главном урле
        assert driver.current_url == Urls.BASE_URL

    # тест на нажатие на логотип Яндекса на странице заказа самоката
    def test_click_logo_yandex(self, driver: WebDriver):

        # открытие страницы
        driver.get(Urls.ORDER_URL)

        # создание объекта страницы HeaderPage
        headerPage = HeaderPage(driver)

        # нажатие на логотип "Яндекс"
        headerPage.click_yandex_logo()

        # создание объекта страницы BasePage
        basePage = BasePage(driver)

        # открытие новой вкладки в браузере
        basePage.open_new_window("ya.ru")

        # проверяем URL новой вкладки
        assert "ya.ru" in driver.current_url
        