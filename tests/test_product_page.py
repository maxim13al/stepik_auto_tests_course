import time
from pages.main_page import MainPage
from pages.product_page import ProductPage


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser, base_url):
        product_page = ProductPage(browser, base_url)
        product_page.open_main_page()
        product_page.click_add_to_basket_btn()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_product_add_to_basket()

