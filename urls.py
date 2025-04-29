from selenium.webdriver.common.by import By

class TestUrl:
    # URL главной (домашней) страницы "Яндекс Самокат"
    URL_HOME_PAGE_YANDEX_SCOOTER = "https://qa-scooter.praktikum-services.ru/"

    # URL страницы заказа самоката "Для кого самокат". "Яндекс Самокат"
    URL_ORDER_SCOOTER_YANDEX_SCOOTER = URL_HOME_PAGE_YANDEX_SCOOTER + "order"

    #URL страницы "Дзен"
    URL_DZEN_PAGE = "https://dzen.ru/?yredirect=true"