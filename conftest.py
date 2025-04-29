import pytest
from selenium import webdriver


# Фикстура для запуска драйвера Firefox и открытие сайта
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

