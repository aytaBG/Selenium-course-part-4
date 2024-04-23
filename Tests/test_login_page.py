import pytest
from .pages.login_page import LoginPage
from .pages.locators import Links

link = Links.LOGIN_PAGE


# тест на наличие формы логина
@pytest.mark.login
def test_should_be_login_form(browser):
    # создаём объект класса LoginPage и открываем в нём ссылку
    page = LoginPage(browser, link)
    page.open()
    # сама проверка
    page.should_be_login_form()


# тест на наличие формы регистрации
@pytest.mark.login
def test_should_be_register_form(browser):
    # создаём объект класса LoginPage и открываем в нём ссылку
    page = LoginPage(browser, link)
    page.open()
    # сама проверка
    page.should_be_register_form()


# тест на правильность ссылки
@pytest.mark.login
def test_is_link_right(browser):
    # создаём объект класса LoginPage и открываем в нём ссылку
    page = LoginPage(browser, link)
    page.open()
    # сама проверка
    page.should_be_login_url()