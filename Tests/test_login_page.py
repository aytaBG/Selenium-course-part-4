import pytest
from Tests.pages.login_page import LoginPage
from Tests.pages.locators import Links

link = Links.LOGIN_PAGE


# тест на наличие формы логина
@pytest.mark.login
def test_should_be_login_form(browser):
    # открываем страницу логина
    page = LoginPage(browser, link)
    page.open()
    # сама проверка
    page.should_be_login_form()


# тест на наличие формы регистрации
@pytest.mark.login
def test_should_be_register_form(browser):
    # открываем страницу логина
    page = LoginPage(browser, link)
    page.open()
    # сама проверка
    page.should_be_register_form()


# тест на правильность ссылки
@pytest.mark.login
def test_is_link_right(browser):
    # открываем страницу логина
    page = LoginPage(browser, link)
    page.open()
    # сама проверка
    page.should_be_login_url()
