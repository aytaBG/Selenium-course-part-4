from Tests.pages.main_page import MainPage
from Tests.pages.login_page import LoginPage
from Tests.pages.basket_page import BasketPage
from Tests.pages.locators import Links
import pytest

# ссыла на главную страницу сайта
link = Links.MAIN_PAGE


# тест возможности перехода на страницу логина
@pytest.mark.main
def test_guest_can_go_to_login_page(browser):
    # открываем главную страницу
    page = MainPage(browser, link)
    page.open()
    # переход на страницу логина
    page.go_to_login_page()
    # необходимо сменить объект с MainPage на LoginPage так как метод
    # should_be_login_page принадлежит классу LoginPage
    login_page = LoginPage(browser, browser.current_url)
    # проверяем правильная ли открылась страница
    login_page.should_be_login_page()


# тест видимости кнопки перехода на страницу логина
@pytest.mark.main
def test_guest_should_see_login_link(browser):
    # открываем главную страницу
    page = MainPage(browser, link)
    page.open()
    # сама проверка
    page.should_be_login_link()


# тест пустоты корзины при первом открытии сайта
@pytest.mark.main
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # открываем главную страницу
    page = MainPage(browser, link)
    page.open()
    # переходим в корзину
    page.go_to_basket()
    # необходимо сменить объект с MainPage на BasketPage так как методы
    # should_be_no_items и should_be_empty_message принадлежат классу BasketPage
    basket_page = BasketPage(browser, browser.current_url)
    # проверяем что нет предметов в корзине
    basket_page.should_be_no_items()
    # проверяем что есть сообщение о пустоте корзины
    basket_page.should_be_empty_message()
