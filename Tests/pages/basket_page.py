from Tests.pages.base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):
    def should_be_no_items(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Корзина не пуста'

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            'Нет сообщения о пустой корзине'