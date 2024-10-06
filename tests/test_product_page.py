import time
import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from selenium.common.exceptions import TimeoutException

class TestProductPage:
    # @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                                             marks=pytest.mark.xfail)])
    # def test_guest_can_add_product_to_basket(self, browser, base_url, link):
    #     base_url = link
    #     product_page = ProductPage(browser, base_url)
    #     product_page.open_main_page()
    #     product_page.click_add_to_basket_btn()
    #     product_page.solve_quiz_and_get_code()
    #     product_page.should_be_product_add_to_basket()
        # time.sleep(600)

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, base_url): 
        product_page = ProductPage(browser, base_url)
        product_page.open_main_page()
        product_page.click_add_to_basket_btn()
        product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, base_url): 
        product_page = ProductPage(browser, base_url)
        product_page.open_main_page()
        product_page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser, base_url): 
        product_page = ProductPage(browser, base_url)
        product_page.open_main_page()
        product_page.click_add_to_basket_btn()
        product_page.should_not_be_success_message_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser, base_url):
        base_url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, base_url)
        page.open_main_page()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page (self, browser, base_url):
        page = ProductPage(browser, base_url)
        page.open_main_page()        
        page.should_be_login_link()
