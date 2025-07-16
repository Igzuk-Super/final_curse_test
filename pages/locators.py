from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form > h2")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form > h2")

class ProductPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    MESSAGE_1 = "has been added to your basket"
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    NAME_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_GO = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    MESSAGE_BASKET_EMPT = "Your basket is empty."
    CONTRNTS_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_TO_BUY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs > div > h2")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    USER_LOGIN = (By.CSS_SELECTOR, "#id_registration-email")
    USER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    USER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "#register_form > button")