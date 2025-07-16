from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def click_button_add_basket(self):
        try:
            assert self.is_element_present(*ProductPageLocators.BASKET_BTN), "Отсутствует кнопка Добавить в корзину"
            add_basket = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
            add_basket.click()
            
            self.solve_quiz_and_get_code()
            
        except TimeoutException:
            print('Кнопка "Добавить в корзину" не обнаружена')
    def product_added(self):
        p_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        try:
            assert ProductPageLocators.MESSAGE_1 in p_message.text, "Ошибка добавления товара"
            print(f'Товар УСПЕШНО добавлен в корзину: {p_message.text}')
        except TimeoutException:
            print('ERR: Ошибка добавления товара')
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Отсутствует название товара"
        prod_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_message = self.browser.find_element(*ProductPageLocators.NAME_MESSAGE)
        try:
            assert prod_name.text == name_message.text, "Название товара не соответсвует добавленному"
            print(f'Название товара в сообщении {prod_name.text} совпадает с тем товаром, который действительно добавили {name_message.text} !')
        except TimeoutException:
            print('ERR: Название товара не соответсвует добавленном!!!')
    def checking_basket_and_price_product(self):
        basket_pr = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        prod_pr = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        try:
            assert prod_pr.text == basket_pr.text, "Стоимость корзины НЕ совпадает с ценой товара"
            print(f'Стоимость корзины {basket_pr.text} совпадает с ценой товара {prod_pr.text}!')
        except TimeoutException:
            print('ERR: Стоимость корзины НЕ совпадает с ценой товара!!!')
    #Проверяем, что нет сообщения об успехе при добавлении товара в корзину
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
    #Если же мы хотим проверить, что какой-то элемент исчезает:
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Element doesn't disappear!!!"