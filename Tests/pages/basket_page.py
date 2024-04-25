from .base_page import BasePage
from .locators import BasketPageLocators


# Page Object страницы корзины
class BasketPage(BasePage):
    # проверка корзины на пустоту
    def should_be_no_items(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'Корзина не пуста'

    # проверка наличия сообщения о пустой корзине
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            'Нет сообщения о пустой корзине'
