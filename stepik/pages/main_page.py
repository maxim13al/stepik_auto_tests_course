from stepik.pages.base_page import BasePage
import time

class MainPage(BasePage):
    LOCATOR = ('xpath', '//a[@id="login_link"]')
    def go_to_login_page(self):
        self.click_element(self.LOCATOR)
    


