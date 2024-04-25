from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_PAGE = (By.CSS_SELECTOR, '.btn-group > .btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    RIGISTER_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    ITEM = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BASKET_ITEM = (By.CSS_SELECTOR, '#messages strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages p > strong')


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')


class Links:
    MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
    LOGIN_PAGE = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    PRODUCT1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    PRODUCT2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    PRODUCT3 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    BASKET = 'http://selenium1py.pythonanywhere.com/basket/'
