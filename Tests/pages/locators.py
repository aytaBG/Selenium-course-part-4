from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    ITEM = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BASKET_ITEM = (By.CSS_SELECTOR, '#messages strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages p > strong')


class Links():
    MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
    LOGIN_PAGE = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    PRODUCT1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    PRODUCT2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    PRODUCT3 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'