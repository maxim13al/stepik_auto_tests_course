from stepik.pages.base_page import BasePage
from stepik.locators.locators import MainPageLocators
import time

class MainPage(BasePage):
    
    def go_to_login_page(self):
        self.click_element(MainPageLocators.LOGIN_LINK)

    def should_be_login_link(self):
        assert self.wait_for_element_to_be_visible(MainPageLocators.LOGIN_LINK)
    

