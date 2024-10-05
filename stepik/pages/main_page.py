from stepik.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    LOCATOR = ('xpath', '//a[@id="login_link"]')

    
    def go_to_login_page(self):
        self.click_element(self.LOCATOR)
    

