from stepik.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    LOGIN_LINK = ('xpath', '//a[@id="login_link"]')
    LOGIN_LINK_INVALID = ('css', '#login_link_invalid')

    
    def go_to_login_page(self):
        self.click_element(self.LOGIN_LINK)

    def should_be_login_link(self):
        assert self.wait_for_element_to_be_visible(self.LOGIN_LINK)
    

