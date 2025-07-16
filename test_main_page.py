import pytest
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

import time

link = "http://selenium1py.pythonanywhere.com"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()                       # выполняем метод страницы — переходим на страницу логина
    
    def test_guest_should_see_login_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()

#------Задание: наследование и отрицательные проверки
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.guest_clik_button_see_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.checks_text_basket_empty()
    basket_page.checks_is_not_product_in_the_basket()
