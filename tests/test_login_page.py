import time
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLoginPage:
    @pytest.mark.xfail
    def test_login_url(self, browser, base_url):
        page = LoginPage(browser, base_url)  
        page.open_main_page()           
        page.should_be_login_url()

    def test_opened_login_form(self, browser, base_url):
        main_page = MainPage(browser, base_url)
        login_page = LoginPage(browser, base_url)
        main_page.open_main_page()
        main_page.go_to_login_page()
        login_page.should_be_login_form()

    def test_opened_register_form(self, browser, base_url):
        main_page = MainPage(browser, base_url)
        login_page = LoginPage(browser, base_url)
        main_page.open_main_page()
        main_page.go_to_login_page()
        login_page.should_be_register_form()


        