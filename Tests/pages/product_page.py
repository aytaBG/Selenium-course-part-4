from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import math


# Page Object страницы товара
class ProductPage(BasePage):
    # добавляем аттрибуты цены и названия товара
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.item = ''
        self.price = ''

    # Метод для решения алёрта
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # проверка нажатия на кнопку "Add to basket"
    def add_item_to_basket_promo(self):
        # находим кнопку "Add to basket" и нажимаем на неё
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        # решаем алёрт
        self.solve_quiz_and_get_code()

    def add_item_to_basket(self):
        # находим кнопку "Add to basket" и нажимаем на неё
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    # задаём цену и названия товара
    def save_item_and_price(self):
        # проверяем наличие названия
        assert self.is_element_present(*ProductPageLocators.ITEM), \
            'Отсутствует название товара'
        # сохраняем название и выводим его в косоль
        self.item = self.browser.find_element(*ProductPageLocators.ITEM).text
        print(f'Название товара {self.item}')
        # проверяем наличие цены
        assert self.is_element_present(*ProductPageLocators.PRICE), \
            'Отсутствует цена товара'
        # сохраняем цену и выводим её в консоль
        self.price = self.browser.find_element(*ProductPageLocators.PRICE).text
        print(f'Цена товара {self.price}')

    # сравниваем цену товара и в корзине
    def check_price(self):
        # проверяем наличие цены в корзине
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), \
            'Нет ценника в корзине'
        # задаём цену в корзине и сравниваем с ценой товара
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert self.price == basket_price, \
            f'Цена в корзине ({basket_price}) не совпадает с ценой товара ({self.price})'
        print(f'Цена в корзине равна {basket_price}')

    # сравниваем название товара и в корзине
    def check_item(self):
        # проверяем наличие товара в корзине
        assert self.is_element_present(*ProductPageLocators.BASKET_ITEM), \
            'Нет ценника в корзине'
        # задаём название товара в корзине и сравниваем с нашим товаром
        basket_item = self.browser.find_element(*ProductPageLocators.BASKET_ITEM).text
        assert self.item == basket_item, \
            f'Товар в корзине ({basket_item}) не совпадает с выбранным ({self.item})'
        print(f'Товар в корзине : {basket_item}')

    # проверка отсутствия сообщения о добавлении товара в корзину
    def is_there_not_a_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ITEM), \
            'Сообщение о добавлении предмета присутствует'

    # проверка исчезновения сообщения о добавлении товара в корзину
    def did_success_message_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_ITEM), \
            'Сооьщение о добавлении предмета не исчезло'
