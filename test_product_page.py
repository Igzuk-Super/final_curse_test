import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

import faker

import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
@pytest.mark.xfail(reason="Bug in this promo-link")
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()                         #открываем страницу
    page.click_button_add_basket()      #нажимам кнопку Добавить в корзину
    page.product_added()                #Сообщение о том, что товар добавлен в корзину & Название товара совпадает с тем, который действительно добавили!
    page.checking_basket_and_price_product()    #Стоимость корзины совпадает с ценой товара.    

# ------Задание: отрицательные проверки
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                         #открываем страницу
    page.click_button_add_basket()      #нажимам кнопку Добавить в корзину
    page.should_not_be_success_message()            #Проверяем, что нет сообщения об успехе

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()                         #открываем страницу
    page.should_not_be_success_message()            #Проверяем, что нет сообщения об успехе

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                         #открываем страницу
    page.click_button_add_basket()      #нажимам кнопку Добавить в корзину
    page.should_dissapear_of_success_message()            #проверить, что какой-то элемент исчезает 

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

#-------Плюсы наследования: пример
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


#------Задание: наследование и отрицательные проверки 
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.guest_clik_button_see_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.checks_text_basket_empty()
    basket_page.checks_is_not_product_in_the_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        self.page = LoginPage(browser, link)
        self.page.open()
        f = faker.Faker()        
        email = f.email()
        password = f.password()        
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, link)
        self.page.open()                         #открываем страницу
        self.page.should_not_be_success_message()            #Проверяем, что нет сообщения об успехе
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, link)
        self.page.open()                         #открываем страницу
        self.page.click_button_add_basket()      #нажимам кнопку Добавить в корзину
        self.page.product_added()                #Сообщение о том, что товар добавлен в корзину & Название товара совпадает с тем, который действительно добавили!
        self.page.checking_basket_and_price_product()    #Стоимость корзины совпадает с ценой товара.    
