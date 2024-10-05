from pages.base_page import BasePage
from locators.locators import ProductPageLocators
import time

class ProductPage(BasePage):
    
    def click_add_to_basket_btn(self):
        self.click_element(ProductPageLocators.ADD_TO_BASKET_BTN)

    def should_be_product_add_to_basket(self):
        self.should_be_message_item_been_added_to_the_basket()
        self.should_be_product_name_in_message_match_added()
        self.should_be_message_with_basket_value()
        self.shold_be_cost_basket_is_same_price_produce()

    def should_be_message_item_been_added_to_the_basket(self):
        assert self.wait_for_element_to_be_visible(ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET)


    def should_be_product_name_in_message_match_added(self):
        assert self.get_element_text(ProductPageLocators.NAME_PRODUCT)\
        in self.get_element_text(ProductPageLocators.MESSAGE_PRODUCT_ADD_TO_BASKET)


    def should_be_message_with_basket_value(self):
        assert self.wait_for_element_to_be_visible(ProductPageLocators.MESSAGE_PRICE_BASKET)

    def shold_be_cost_basket_is_same_price_produce(self):
        assert self.get_element_text(ProductPageLocators.PRICE_PRODUCT)\
        in self.get_element_text(ProductPageLocators.MESSAGE_PRICE_BASKET)



    