import pytest
from .pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/accounts/login/'


@pytest.mark.login
def test_should_be_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


@pytest.mark.login
def test_should_be_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


@pytest.mark.login
def test_is_link_right(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()