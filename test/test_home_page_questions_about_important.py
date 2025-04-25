import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from urls import TestUrl
from locators.home_page_locators import TLHP
from pages.home_page import HomePage
from data import QA

class TestImportantQuestions:

    @pytest.mark.parametrize(
        "locator_question, locator_answer, answer_text",
        [
            (TLHP.LOCATOR_HOW_IT_COST, TLHP.LOCATOR_HOW_IT_COST_TEXT, QA.HOW_MUCH_COST),
            (TLHP.LOCATOR_SEVERAL_SCOOTER, TLHP.LOCATOR_SEVERAL_SCOOTER_TEXT, QA.SEVERAL_SCOOTER),
            (TLHP.LOCATOR_RENTAL_TIME_CALCULATION, TLHP.LOCATOR_RENTAL_TIME_CALCULATION_TEXT, QA.RENTAL_TIME_CALCULATION),
            (TLHP.LOCATOR_ORDER_SCOOTER_TODAY, TLHP.LOCATOR_ORDER_SCOOTER_TODAY_TEXT, QA.ORDER_SCOOTER_TODAY),
            (TLHP.LOCATOR_EXTEND_OR_RETURN_SCOOTER, TLHP.LOCATOR_EXTEND_OR_RETURN_SCOOTER_TEXT, QA.EXTEND_OR_RETURN_SCOOTER),
            (TLHP.LOCATOR_CHARGING_SCOOTER, TLHP.LOCATOR_CHARGING_SCOOTER_TEXT, QA.CHARGING_SCOOTER),
            (TLHP.LOCATOR_CANCEL_ORDER, TLHP.LOCATOR_CANCEL_ORDER_TEXT, QA.CANCEL_ORDER),
            (TLHP.LOCATOR_OUTSIDE_MKAD, TLHP.LOCATOR_OUTSIDE_MKAD_TEXT, QA.OUTSIDE_MKAD)
        ]
    )

    def test_questions_about_important(self, driver, locator_question, locator_answer, answer_text):
        page = HomePage(driver)
        # открыть сайт
        page.open_site()
        # проскролить до элемента и кликнуть его
        page.scroll_to_element(locator_question)
        # дождаться пока текст появится на странице, проверить на соответствие ОР и ФР
        WebDriverWait(page.driver, 10).until(
            EC.text_to_be_present_in_element(locator_answer, answer_text)
        )
        real_text = page.get_text_from_element(locator_answer)
        expect_text = answer_text
        assert real_text == expect_text
