from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = ("css", "#login_link")
    LOGIN_LINK_INVALID = ("css", "#login_link_inc")


class LoginPageLocators:
    ENTER_BTN = ("xpath", "//button[@name='login_submit']")
    REGISTRATION_BTN = ("xpath", "//button[@name='registration_submit']")
    LOGIN_LINK = ('css', '#login_link')
    LOGIN_LINK_INVALID = ('css', '#login_link_invalid')

class MainPageLocators:
    LOGIN_LINK = ('css', '#login_link')
    LOGIN_LINK_INVALID = ('css', '#login_link_invalid')

class ProductPageLocators:
    ADD_TO_BASKET_BTN = ("xpath", "//button[contains(@class, 'btn-add-to-basket')]")
    MESSAGE_PRODUCT_ADD_TO_BASKET = ("xpath", "//div[@id='messages']/div[1]")
    MESSAGE_PRICE_BASKET = ("xpath", "//div[@id='messages']/div[3]")
    NAME_PRODUCT = ("xpath", "//div[contains(@class, 'product_main')]/h1")
    PRICE_PRODUCT = ("xpath", "//p[@class = 'price_color']")


