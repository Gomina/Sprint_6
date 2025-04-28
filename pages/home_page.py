import pytest
import allure
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from data import QA
from urls import TestUrl
from locators.home_page_locators import TLHP
from locators.order_scooter_page_locators import TLOS


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # Создаем экземпляр WebDriverWait с таймаутом 10 секунд
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step('метод открывает сайт на главной странице')
    def open_site(self):
        self.driver.get(TestUrl.URL_HOME_PAGE_YANDEX_SCOOTER)

    @allure.step('метод закрывает куки')
    def close_cookies(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(TLHP.LOCATOR_CLOSE_COOKIES)).click()

    @allure.step('метод находить нужный элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    @allure.step('метод кликает по нужному элементы')
    def clic_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('метод скроллит до нужного элемента и кликает его')
    def scroll_to_element(self, locator):
        # Ждём появления элемента на странице
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )

        # Прокручиваем до элемента
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Кликаем по элементу через JavaScript
        self.driver.execute_script("arguments[0].click();", element)
        # Возврат найденного элемента
        return element

    @allure.step('метод возвращает текст элементы')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('метод вставляет текст в элемент')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('метод ожидает загрузку элемента с текстом')
    def waiting_text_in_elements_to_load(self, locator_answer,answer_text):
        # Дождаться появления элемента с текстом
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator_answer, answer_text)
        )

    @allure.step('метод ожидает загрузку конкретного url')
    def loading_page_with_url(self, url):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(url)
        )

    @allure.step('метод дожидается открытия нового окна и переключается на него')
    def witch_to_new_open_window(self):
        # дождаться появления нового окна (вкладки)
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        # переключиться на последнее открытое окно (вкладку)
        new_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window_handle)