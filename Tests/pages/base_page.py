from Tests.pages.locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # инициализация объекта
    def __init__(self, browser, url, timeout=10):
        # объект browser создаётся в conftest.py
        self.browser = browser
        # ссылка передаётся из теста
        self.url = url
        # время для ожидания, по умолчанию 10
        if timeout != 0:
            self.browser.implicitly_wait(timeout)

    # переход на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET_PAGE)
        basket.click()

    # проверить, есть ли кнопка перехода на страницу логина
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            'Ссылка логина отсутствует'

    # открыть страницу по ссылке
    def open(self):
        self.browser.get(self.url)

    # проверить существует ли элемент
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
