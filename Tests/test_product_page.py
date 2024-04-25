from Tests.pages.basket_page import BasketPage
from Tests.pages.login_page import LoginPage
from Tests.pages.product_page import ProductPage
from Tests.pages.locators import Links
import pytest
import time

# ссылка на товар, не содержащий промо-акций
link = Links.PRODUCT


# тесты для зарегистрированных пользователей
@pytest.mark.product
class TestUserAddToBasketFromProductPage:
    # настройка браузера
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        # открытие страницы регистрации
        link = Links.LOGIN_PAGE
        page = LoginPage(browser, link)
        page.open()
        # задаём случайным пароль и имейл
        password = str(time.time())
        email = password + "@fakemail.org"
        # регистрируемся
        page.register_new_user(email, password)
        # проверяем регистрацию
        page.should_be_authorized_user()

    # тест возможности добавления товара в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # открываем страницу с товаром
        page = ProductPage(browser, link)
        page.open()
        # сохраняем название и цену товара для проверки
        page.save_item_and_price()
        # добавляем товар в корзину
        page.add_item_to_basket()
        # проверяем, совпадает ли цена и название
        page.check_price()
        page.check_item()

    # проверяем, что при открытии страницы нет сообщения о добавлении товара в корзину
    def test_user_cant_see_success_message(self, browser):
        # открываем страницу с товаром (убираем неявное ожидание, так как проверка ставит своё)
        page = ProductPage(browser, link, timeout=0)
        page.open()
        # проверяем, что сообщение не появляется просто так
        page.is_there_not_a_success_message()


# тест на добавление товаров с разными промо-акциями в корзину
@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/" +
                                               "catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.product
def test_guest_can_add_product_to_basket_promo(browser, link):
    # открываем страницу товара
    page = ProductPage(browser, link)
    page.open()
    # сохраняем название и цену товара для проверки
    page.save_item_and_price()
    # добавляем товар в корзину и решаем капчу
    page.add_item_to_basket_promo()
    # проверяем, совпадает ли цена и название
    page.check_price()
    page.check_item()


# тест возможности добавления товара в корзину
@pytest.mark.need_review
@pytest.mark.product
def test_guest_can_add_product_to_basket(browser):
    # открываем страницу товвра
    page = ProductPage(browser, link)
    page.open()
    # сохраняем название и цену товара для проверки
    page.save_item_and_price()
    # добавляем товар в корзину
    page.add_item_to_basket()
    # проверяем, совпадает ли цена и название
    page.check_price()
    page.check_item()


# тест на отсутствие сообщения о добавлении товара в корзину после добавления товара в корзину
@pytest.mark.xfail
@pytest.mark.product
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # открываем страницу с товаром (убираем неявное ожидание, так как проверка ставит своё)
    page = ProductPage(browser, link, timeout=0)
    page.open()
    # добавляем товар в корзину
    page.add_item_to_basket()
    # проверка отсутствия сообщения о добавлении товара в корзину
    page.is_there_not_a_success_message()


# проверяем, что при открытии страницы нет сообщения о добавлении товара в корзину
@pytest.mark.product
def test_guest_cant_see_success_message(browser):
    # открываем страницу с товаром (убираем неявное ожидание, так как проверка ставит своё)
    page = ProductPage(browser, link, timeout=0)
    page.open()
    # проверяем, что сообщение не появляется просто так
    page.is_there_not_a_success_message()


# тест на исчезновении сообщения о добавлении товара в корзину
@pytest.mark.xfail
@pytest.mark.product
def test_message_disappeared_after_adding_product_to_basket(browser):
    # открываем страницу с товаром (убираем неявное ожидание, так как проверка ставит своё)
    page = ProductPage(browser, link, timeout=0)
    page.open()
    # добавляем товар в корзину
    page.add_item_to_basket()
    # ждём исчёзнолвения сообщения о добавлении товара в корзину
    page.did_success_message_dissapear()


# тест на видимость книпки перехода на страницу логина
@pytest.mark.product
def test_guest_should_see_login_link_on_product_page(browser):
    # открываем страницу с товаром
    page = ProductPage(browser, link)
    page.open()
    # находим кнопку страницы логина
    page.should_be_login_link()


@pytest.mark.product
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # открываем страницу с товаром
    page = ProductPage(browser, link)
    page.open()
    # переход на страницу логина
    page.go_to_login_page()
    # необходимо сменить объект с ProductPage на LoginPage так как метод
    # should_be_login_page принадлежит классу LoginPage
    login_page = LoginPage(browser, browser.current_url)
    # проверяем правильная ли открылась страница
    login_page.should_be_login_page()


# тест пустоты корзины при первом открытии сайта
@pytest.mark.product
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # открываем страницу с товаром
    page = ProductPage(browser, link)
    page.open()
    # переходим в корзину
    page.go_to_basket()
    # необходимо сменить объект с ProductPage на BasketPage так как методы
    # should_be_no_items и should_be_empty_message принадлежат классу BasketPage
    basket_page = BasketPage(browser, browser.current_url)
    # проверяем что нет предметов в корзине
    basket_page.should_be_no_items()
    # проверяем что есть сообщение о пустоте корзины
    basket_page.should_be_empty_message()
