from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # метод открытия новой вкладки в браузере (сделан с помощью ии)
    def open_new_window(self, url):
        # ждём появления новой вкладки
        self.wait.until(lambda d: len(d.window_handles) > 1)

        # переключаемся на другую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # ждём загрузки
        self.wait.until(lambda d: d.current_url != "about:blank")
        self.wait.until(expected_conditions.url_contains(url))

    # метод поиска всех элементов с ожиданием
    def find_all(self, locator):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(locator))

    # скролл до элемента
    def scroll_to(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    # метод ввода текста в поле с ожиданием
    def send_keys(self, locator, text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    # метод нажатия на элемент с ожидаем кликабельности
    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    # JS клик на элемент с ожидаем кликабельности
    def js_click(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    # метод получения текстового значения
    def get_text(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

    # метод открытия страницы
    def open(self, url):
        self.driver.get(url)

    # метод получения текущего урла
    def get_current_url(self):
        return self.driver.current_url
