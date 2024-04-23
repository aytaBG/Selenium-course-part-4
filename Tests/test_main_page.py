from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import Links
import pytest

link = Links.MAIN_PAGE


# тест возможности перехода на страницу логина
@pytest.mark.main
def test_guest_can_go_to_login_page(browser):
    # создаём объект класса MainPage и открываем в нём ссылку
    page = MainPage(browser, link)
    page.open()
    # переход на страницу логина
    page.go_to_login_page()
    # создаём объект LoginPage и передаём в него текущее окно и ссылку
    # необходимо сменить объект с MainPage на LoginPage так как метод
    # should_be_login_page принадлежит классу LoginPage
    login_page = LoginPage(browser, browser.current_url)
    # проверяем правильная ли открылась страница
    login_page.should_be_login_page()


# тест видимости кнопки перехода на страницу логина
@pytest.mark.main
def test_guest_should_see_login_link(browser):
    # создаём объект MainPage и открываем в нём ссылку
    page = MainPage(browser, link)
    page.open()
    #сама проверка
    page.should_be_login_link()