from Tests.pages.basket_page import BasketPage
from Tests.pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import Links
import pytest
import time

link = Links.PRODUCT3

@pytest.mark.new
@pytest.mark.product
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = Links.LOGIN_PAGE
        password = str(time.time())
        email = password + "@fakemail.org"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.save_item_and_price()
        page.add_item_to_basket()
        page.check_price()
        page.check_item()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link, timeout=0)
        page.open()
        page.is_there_not_a_success_message()

# тест на добавление товара в корзину
@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.product
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.save_item_and_price()
    page.add_item_to_basket_promo()
    page.check_price()
    page.check_item()

@pytest.mark.xfail
@pytest.mark.product
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_item_to_basket()
    page.is_there_not_a_success_message()

@pytest.mark.product
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.is_there_not_a_success_message()

@pytest.mark.xfail
@pytest.mark.product
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_item_to_basket()
    page.did_success_message_dissapear()

@pytest.mark.product
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.product
def test_guest_can_go_to_login_page_from_product_page(browser):
    # создаём объект класса ProductPage и открываем в нём ссылку
    page = ProductPage(browser, link)
    page.open()
    # переход на страницу логина
    page.go_to_login_page()
    # создаём объект LoginPage и передаём в него текущее окно и ссылку
    # необходимо сменить объект с ProductPage на LoginPage так как метод
    # should_be_login_page принадлежит классу LoginPage
    login_page = LoginPage(browser, browser.current_url)
    # проверяем правильная ли открылась страница
    login_page.should_be_login_page()

@pytest.mark.product
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items()
    basket_page.should_be_empty_message()
