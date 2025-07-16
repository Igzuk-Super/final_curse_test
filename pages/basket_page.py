from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    #проверяет что в корзине нет товара
    def checks_is_not_product_in_the_basket(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS_TO_BUY_MESSAGE), "В корзине ЕСТЬ товар!"
    #проверяет текст что корзина пуста:
    def checks_text_basket_empty(self):
        p_basket = self.browser.find_element(*BasePageLocators.CONTRNTS_BASKET)
        assert BasePageLocators.MESSAGE_BASKET_EMPT in p_basket.text, "Корзина НЕ пуста!"