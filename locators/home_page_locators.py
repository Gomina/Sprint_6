from selenium.webdriver.common.by import By

class TLHP:

    # Кнопка, закрывающая куки. "да все привыкли"
    LOCATOR_CLOSE_COOKIES = By.ID, "rcc-confirm-button"

    # Выпадающий список. "Сколько это стоит? И как оплатить?"
    LOCATOR_HOW_IT_COST = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'Сколько это стоит?')]"

    # Выпадающий список. Ответ выпадающего списка "Сколько это стоит? И как оплатить?"
    LOCATOR_HOW_IT_COST_TEXT = By.XPATH, "//p[contains(text(), 'Сутки — 400 рублей.')]"

    # Выпадающий список.  "Хочу сразу несколько самокатов! Так можно?"
    LOCATOR_SEVERAL_SCOOTER = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'Хочу сразу несколько самокатов!')]"

    #Выпадающий список. Ответ выпадающего списка "Хочу сразу несколько самокатов! Так можно?"
    LOCATOR_SEVERAL_SCOOTER_TEXT = By.XPATH, "//p[contains(text(), 'Пока что у нас так: один заказ — один самокат.')]"

    # Выпадающий список. "Как рассчитывается время аренды?"
    LOCATOR_RENTAL_TIME_CALCULATION = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'Как рассчитывается время')]"

    # Выпадающий список. Ответ выпадающего списка "Как рассчитывается время аренды?"
    LOCATOR_RENTAL_TIME_CALCULATION_TEXT = By.XPATH, "//p[contains(text(), 'Допустим, вы оформляете заказ')]"

    # Выпадающий список. "Можно ли заказать самокат прямо на сегодня?"
    LOCATOR_ORDER_SCOOTER_TODAY = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'Можно ли заказать самокат')]"

    # Выпадающий список. Ответ выпадающего списка "Можно ли заказать самокат прямо на сегодня?"
    LOCATOR_ORDER_SCOOTER_TODAY_TEXT = By.XPATH, "//p[contains(text(), 'Только начиная с завтрашнего дня.')]"

    # Выпадающий список. "Можно ли продлить заказ или вернуть самокат раньше?"
    LOCATOR_EXTEND_OR_RETURN_SCOOTER = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'продлить заказ или вернуть самокат раньше')]"

    # Выпадающий список. Ответ выпадающего списка "Можно ли заказать самокат прямо на сегодня?"
    LOCATOR_EXTEND_OR_RETURN_SCOOTER_TEXT = By.XPATH, "//p[contains(text(), 'Пока что нет!')]"

    # Выпадающий список. "Вы привозите зарядку вместе с самокатом?"
    LOCATOR_CHARGING_SCOOTER =  By.XPATH, "//div[@class='accordion__button' and contains(text(), 'зарядку вместе с самокатом')]"

    # Выпадающий список. Ответ выпадающего списка "Можно ли заказать самокат прямо на сегодня?"
    LOCATOR_CHARGING_SCOOTER_TEXT = By.XPATH, "//p[contains(text(), 'приезжает к вам с полной зарядкой')]"

    # Выпадающий список. "Можно ли отменить заказ?"
    LOCATOR_CANCEL_ORDER = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'отменить заказ')]"

    # Выпадающий список. Ответ выпадающего списка "Можно ли отменить заказ?"
    LOCATOR_CANCEL_ORDER_TEXT = By.XPATH, "//p[contains(text(), 'Да, пока самокат не привезли.')]"

    # Выпадающий список. "Я жизу за МКАДом, привезёте?"
    LOCATOR_OUTSIDE_MKAD = By.XPATH, "//div[@class='accordion__button' and contains(text(), 'МКАДом, привезёте?')]"

    # Выпадающий список. Ответ выпадающего списка "Я жизу за МКАДом, привезёте?"
    LOCATOR_OUTSIDE_MKAD_TEXT = By.XPATH, "//p[contains(text(), 'И Москве, и Московской области.')]"

    # Домашняя страница. Шапка сайта. Кнопка "Заказать"
    LOCATOR_ORDER_BUTTON_CAP = By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']"

    # Домашняя страница. Блок "Как это работает". Кнопка "Заказать"
    LOCATOR_ORDER_BUTTON_HOW_IT_WORKS = By.CSS_SELECTOR, ".Home_FinishButton__1_cWm > button.Button_Button__ra12g"