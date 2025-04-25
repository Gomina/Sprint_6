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
from data import TD
from urls import TestUrl
from locators.home_page_locators import TLHP
from locators.order_scooter_page_locators import TLOS
from pages.home_page import HomePage

class OrderPage(HomePage):

    @allure.title('метод, открывающий форму заказа')
    def open_order_form(self, locator):
        # открыть сайт
        self.open_site()
        # найти кнопку для входа в форму заказа и кликнуть по ней
        self.clic_on_element(locator)

    @allure.title('метод, кликающий на поле и вставляющий в поле значение')
    def fill_in_field(self, locator, data):
        self.clic_on_element(locator)
        self.set_text_to_element(locator,data)

    @allure.step('шаг, заполняющий форму заказа на странице "Для кого самокат"')
    def filling_form_whom_the_scooter(self, user_data=None):
        # вставить Имя
        self.fill_in_field(TLOS.LOCATOR_FIELD_NAME, user_data["name"])
        # вставить Фамилию
        self.fill_in_field(TLOS.LOCATOR_FIELD_SURNAME, user_data["surname"])
        # вставить Адрес
        self.fill_in_field(TLOS.LOCATOR_FIELD_ADDRESS, user_data["address"])
        # вставить метро
        self.clic_on_element(TLOS.LOCATOR_FIELD_METRO)
        self.scroll_to_element(TLOS.LOCATOR_PROSPEKT_VERNADSKOGO)
        self.clic_on_element(TLOS.LOCATOR_PROSPEKT_VERNADSKOGO)
        # вставить телефон
        self.fill_in_field(TLOS.LOCATOR_FIELD_PHONE, user_data["phone"])
        # нажать кнопку "Далее"
        self.clic_on_element(TLOS.LOCATOR_BUTTON_NEXT)

    @allure.step('шаг, заполняющий форму заказа на странице "Про аренду"')
    def filling_form_about_rent(self, comment_for_courier):
        # выбрать дату доставки самоката
        self.clic_on_element(TLOS.LOCATOR_FIELD_RENTAL_START)
        self.clic_on_element(TLOS.LOCATOR_RENTAL_START_DATE)
        # выбрать срок аренды самоката
        self.clic_on_element(TLOS.LOCATOR_FIELD_RENTAL_PERIOD)
        self.clic_on_element(TLOS.LOCATOR_TWO_DAYS)
        # выбрать цвет самоката
        self.clic_on_element(TLOS.LOCATOR_FIELD_SCOOTER_COLOR)
        # добавить комментарий для курьера
        self.fill_in_field(TLOS.LOCATOR_FIELD_COMMENT_FOR_COURIER, comment_for_courier)
        # нажать кнопку "Заказать". Кнопка расположена под блоком "Про аренду"
        self.clic_on_element(TLOS.LOCATOR_ORDER_BUTTON)