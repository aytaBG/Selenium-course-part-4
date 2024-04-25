from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # проверка является ли страница верной
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверка верна ли ссылка
    def should_be_login_url(self):
        assert self.browser.current_url.find('login'), \
            'Неверная ссылка'

    # проверка наличия формы для логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'Форма для логина отсутствует'

    # проверка наличия формы для регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'Форма для регистрации отсутствует'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.RIGISTER_BUTTON).click()
