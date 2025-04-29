import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import QA
from urls import TestUrl
from pages.home_page import HomePage
from pages.order_scooter_page import OrderPage
from locators.home_page_locators import  TLHP
from locators.order_scooter_page_locators import TLOS
from data import TD

class TestOrderScooter:

    @allure.title('Возможно сделать заказ через кнопку "Заказать", расположенную в шапке сайта')
    def test_order_button_in_header(self, driver):
        page = OrderPage(driver)
        # кликнуть на кнопку "Заказать" в шапке сайта
        page.open_order_form(TLHP.LOCATOR_ORDER_BUTTON_CAP)
        # используем второй набор данных (DATA_SET_2)
        user_data = TD.DATA_SET_2
        # заполнить форму с данными из DATA_SET_2
        page.filling_form_whom_the_scooter(user_data=user_data)
        page.filling_form_about_rent(comment_for_courier=user_data["comment_for_courier"])
        # нажать на кнопку "Да"
        page.clic_on_element(TLOS.LOCATOR_BUTTON_YES)
        # дождаться появления окна "Заказ оформлен"
        page.waiting_text_in_elements_to_load(TLOS.LOCATOR_WINDOW_ORDER_PLACED, TD.WINDOW_ORDER_PLACED)
        # на странице появляется окно с текстом "Заказ оформлен"
        current_text = driver.find_element(*TLOS.LOCATOR_WINDOW_ORDER_PLACED).text
        # проверка наличия заголовка "Заказ оформлен" в тексте окна
        expected_text = TD.WINDOW_ORDER_PLACED
        assert expected_text in current_text




    @allure.title('Возможно сделать заказ через кнопку "Заказать", расположенную в блоке "Как это работает"')
    def test_order_button_in_how_this_work(self, driver):
        page = OrderPage(driver)
        page.open_site()
        # использовать первый набор данных (DATA_SET_1)
        user_data = TD.DATA_SET_1
        # проскролить и кликнуть на кнопку "Заказать" в блоке "Как это работает"
        page.scroll_to_element(TLHP.LOCATOR_ORDER_BUTTON_HOW_IT_WORKS)
        # заполнить форму с данными из DATA_SET_1
        page.filling_form_whom_the_scooter(user_data=user_data)
        page.filling_form_about_rent(comment_for_courier=user_data["comment_for_courier"])
        # нажать на кнопку "Да"
        page.clic_on_element(TLOS.LOCATOR_BUTTON_YES)
        # дождаться появления окна "Заказ оформлен"
        page.waiting_text_in_elements_to_load(TLOS.LOCATOR_WINDOW_ORDER_PLACED, TD.WINDOW_ORDER_PLACED)
        # на странице появляется окно с текстом "Заказ оформлен"
        current_text = driver.find_element(*TLOS.LOCATOR_WINDOW_ORDER_PLACED).text
        # проверка наличия заголовка "Заказ оформлен" в тексте окна
        expected_text = TD.WINDOW_ORDER_PLACED
        assert expected_text in current_text

    @allure.title('После успешного заказа, если нажать на логотип «Самоката», осуществляется переход на главную страницу «Самоката»')
    def test_click_logo_home_page(self, driver):
        page = OrderPage(driver)
        # кликнуть на кнопку "Заказать" в шапке сайта
        page.open_order_form(TLHP.LOCATOR_ORDER_BUTTON_CAP)
        # используем второй набор данных (DATA_SET_1)
        user_data = TD.DATA_SET_1
        # заполнить форму с данными из DATA_SET_2
        page.filling_form_whom_the_scooter(user_data=user_data)
        page.filling_form_about_rent(comment_for_courier=user_data["comment_for_courier"])
        # нажать на кнопку "Да"
        page.clic_on_element(TLOS.LOCATOR_BUTTON_YES)
        # кликнуть "Посмотреть статус" окно "Заказ оформлен"
        page.clic_on_element(TLOS.LOCATOR_BUTTON_VIEW_STATUS)
        # кликнуть "Самокат" страница "Статус заказа"
        page.clic_on_element(TLOS.LOCATOR_SCOOTER_LOGO)
        # дождаться загрузки домашней страницы
        page.loading_page_with_url(TestUrl.URL_HOME_PAGE_YANDEX_SCOOTER)
        # проверить, что открылась домашняя страница
        current_url = driver.current_url
        expected_url = TestUrl.URL_HOME_PAGE_YANDEX_SCOOTER
        assert current_url == expected_url

    @allure.title('После успешного заказа, если нажать на логотип Яндекса, откроется главная страница Дзена')
    def test_click_yandex_open_dzen(self, driver):
        page = OrderPage(driver)
        # кликнуть на кнопку "Заказать" в шапке сайта
        page.open_order_form(TLHP.LOCATOR_ORDER_BUTTON_CAP)
        # используем второй набор данных (DATA_SET_1)
        user_data = TD.DATA_SET_1
        # заполнить форму с данными из DATA_SET_2
        page.filling_form_whom_the_scooter(user_data=user_data)
        page.filling_form_about_rent(comment_for_courier=user_data["comment_for_courier"])
        # нажать на кнопку "Да"
        page.clic_on_element(TLOS.LOCATOR_BUTTON_YES)
        # кликнуть "Посмотреть статус" окно "Заказ оформлен"
        page.clic_on_element(TLOS.LOCATOR_BUTTON_VIEW_STATUS)
        # кликнуть "Яндекс" страница "Статус заказа"
        page.clic_on_element(TLOS.LOCATOR_YANDEX_LOGO)
        # дождаться появления нового окна (вкладки) и переключиться на него
        page.witch_to_new_open_window()
        # проверить, дождаться чтобы URL "Дзена" прогрузился
        page.loading_page_with_url(TestUrl.URL_DZEN_PAGE)
        # проверить, что открылась страница Дзен
        current_url = driver.current_url
        expected_url = TestUrl.URL_DZEN_PAGE
        assert current_url == expected_url