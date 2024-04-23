from selenium.common.exceptions import NoSuchElementException


class BasePage():
    # инициализация объекта
    def __init__(self, browser, url, timeout=10):
        # объект browser создаётся в conftewst.py
        self.browser = browser
        # ссылка передаётся из теста
        self.url = url
        # время для ожидан8ия, по умолчанию 10
        self.browser.implicitly_wait(timeout)

    # открыть страницу по ссылке
    def open(self):
        self.browser.get(self.url)

    # проверить существует ли элемент
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True



