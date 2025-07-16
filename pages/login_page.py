from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Invalid login page address"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        link = self.browser.find_element(*BasePageLocators.USER_LOGIN)
        link.send_keys(email)
        link = self.browser.find_element(*BasePageLocators.USER_PASSWORD1)
        link.send_keys(password)
        link = self.browser.find_element(*BasePageLocators.USER_PASSWORD2)
        link.send_keys(password)
        link = self.browser.find_element(*BasePageLocators.REGISTER_BTN)
        link.click()