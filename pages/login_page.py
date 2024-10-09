from pages.base_page import BasePage
from locators.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.base_url in self.get_current_url()

    def should_be_login_form(self):
        assert self.wait_for_element_to_be_visible(LoginPageLocators.ENTER_BTN)

    def should_be_register_form(self):
        assert self.wait_for_element_to_be_visible(LoginPageLocators.REGISTRATION_BTN)