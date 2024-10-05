from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from stepik.pages.main_page import MainPage
from selenium import webdriver

class TestMainPage:
    def test_guest_can_go_to_login_page(self, browser, base_url):
        page = MainPage(browser, base_url)  
        page.open_main_page()           
        page.should_be_login_link()
        # page.go_to_login_page()
        

     


