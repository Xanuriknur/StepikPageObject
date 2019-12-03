from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_basket_summary(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY),\
            "Basket summory, but should not be"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY_BASKET),\
            "Text 'empty basket' is not present"