from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators, Links
import pytest

link = Links.PRODUCT3


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