from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # метод открытия новой вкладки в браузере (сделан с помощью ии)
    def open_new_window(self, url):
        # ждём появления новой вкладки
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)

        # переключаемся на другую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # ждём загрузки
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != "about:blank")
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))
