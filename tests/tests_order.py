import pytest
import allure
from pages.home_page import HomePage
from pages.header_page import HeaderPage
from pages.order_page import OrderPage
from pages.modal_page import ModalPage
from data.urls import Urls
from data.data_test import ORDER_DATA_1, ORDER_DATA_2
from selenium.webdriver.chrome.webdriver import WebDriver

@allure.title('Список тестов по созданию заказов на самокаты')
class TestOrder:

    # параметризированный тест с нажатием на кнопку "Заказать" в хедере
    @allure.title('Оформление заказа через кнопку "Заказать" в хедере')
    @allure.description('Проверяем, что при клике по кнопке "Заказать" в хедере открывается страница заказа и заказ успешно оформляется')
    @pytest.mark.parametrize("order_data", [ORDER_DATA_1, ORDER_DATA_2])
    def test_scooter_order(self, driver: WebDriver, order_data):
        
        with allure.step('Открытие главной страницы'):
            headerPage = HeaderPage(driver)
            headerPage.open(Urls.BASE_URL)

        with allure.step('Нажатие на кнопку "Заказать" в хедере'):
            headerPage.click_order_button()

        with allure.step('Проверка, что находимся на урле заказа самоката'):
            assert headerPage.get_current_url() == Urls.ORDER_URL

        with allure.step('Заполнение формы заказа самоката'):
            orderPage = OrderPage(driver)
            orderPage.order_about_client(order_data)
            orderPage.order_about_rental(order_data)

        with allure.step('Нажимает на кнопку "Да" в модальном окне "Хотите оформить заказ?"'):
            modalPage = ModalPage(driver)
            modalPage.click_yes_button()

        with allure.step('Проверка отображения модального окна "Заказ оформлен"'):
            order_modal_header = modalPage.get_order_modal_header()
            assert 'Заказ оформлен' in order_modal_header

    # тест на нажатие на логотип Самокат на странице заказа самоката
    @allure.title('Логотип Самоката возвращает на главную страницу')
    @allure.description('На странице заказа кликаем по логотипу Самоката и проверяем, что открывается главная страница')
    def test_click_logo_scooter(self, driver: WebDriver):

        with allure.step('Открытие главной страницы'):
            homePage = HomePage(driver)
            homePage.open(Urls.BASE_URL)

        with allure.step('Нажатие на кнопку "Заказать" на главной странице'):
            homePage.click_order_button()

        with allure.step('Проверка, что находимся на урле заказа самоката'):
            assert homePage.get_current_url() == Urls.ORDER_URL

        with allure.step('Нажатие на логотип "Скутер" в хедере на странице заказа самоката'):
            headerPage = HeaderPage(driver)
            headerPage.click_scooter_logo()

        with allure.step('Проверка редиректа на главную страницу'):
            assert headerPage.get_current_url() == Urls.BASE_URL

    # тест на нажатие на логотип Яндекса на странице заказа самоката
    @allure.title('Логотип Яндекса открывает новую вкладку в браузере')
    @allure.description('На странице заказа кликаем по логотипу Яндекса и проверяем, что открывается новая вкладка в браузере')
    def test_click_logo_yandex(self, driver: WebDriver):

        with allure.step('Открытие страницы заказа самоката'):
            headerPage = HeaderPage(driver)
            headerPage.open(Urls.ORDER_URL)

        with allure.step('Нажатие на логотип "Яндекс" в хедере на странице заказа самоката'):
            headerPage.click_yandex_logo()

        with allure.step('Проверка открытия новой вкладки браузера'):
            headerPage.open_new_window("ya.ru")
            assert "ya.ru" in headerPage.get_current_url()
        