import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    chrome_options = webdriver.FirefoxOptions() # создали объект для опций
    driver = webdriver.Firefox(options=chrome_options) # создали драйвер и передали в него настройки

    yield driver

    driver.quit()
