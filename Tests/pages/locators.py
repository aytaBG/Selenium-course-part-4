from selenium.webdriver.common.by import By


# базовые локаторы
class BasePageLocators:
    # кнопка перехода на страницу логина
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    # кнопка перехода в корзину
    BASKET_PAGE = (By.CSS_SELECTOR, '.btn-group > .btn-default')
    # иконка пользователя
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# локаторы основной страницы
class MainPageLocators:
    # :C
    pass


# локаторы страницы логина
class LoginPageLocators:
    # форма логина
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    # форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    # поле для имейла (регистрация)
    REGISTER_EMAIL = (By.ID, 'id_registration-email')
    # поле для пароля (регистрация)
    REGISTER_PASSWORD = (By.ID, 'id_registration-password1')
    # поле для подтверждения пароля
    REGISTER_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    # кнопка завершения регистрации
    RIGISTER_BUTTON = (By.NAME, 'registration_submit')


# локаторы страницы с товаром
class ProductPageLocators:
    # кнопка добавления в корзину
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    # название товара
    ITEM = (By.CSS_SELECTOR, '.product_main > h1')
    # цена товара
    PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    # название товара, добавленного в корзину
    BASKET_ITEM = (By.CSS_SELECTOR, '#messages strong')
    # цена товара, добавленного в корзину
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages p > strong')


# локаторы корзины
class BasketPageLocators:
    # сообщение о пустой корзине
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    # товары в корзине
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')


# ссылки
class Links:
    # главная страница
    MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
    # страница логина
    LOGIN_PAGE = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    # страница товара
    PRODUCT = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    # страница корзины
    BASKET = 'http://selenium1py.pythonanywhere.com/basket/'
