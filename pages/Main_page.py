from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
from config import TestData

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

# Определение локаторов элементов на главной странице

    # Главный логотип
    MAIN_LOGO = (By.CSS_SELECTOR, "#app-header > div > div > svg")
    
    # Вкладка "Почта"
    MAIL = (By.XPATH, "//*[@id='t-btn-tab-mail']")
    
    # Поле для ввода имени пользователя
    USERNAME = (By.XPATH, '// *[ @ id = "username"]')
    
    # Поле для ввода пароля
    PASS = (By.XPATH, '//*[@id="password"]')
    
    # Кнопка "Вход"
    BUTTON_INPUT = (By.XPATH, '//*[@id="kc-login"]')
    
    # Кнопка "Выход"
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "#logout-btn")
    
    # Сообщение об ошибке для имени пользователя и пароля
    ERROR_USERNAME_PASS = (By.XPATH, '// *[ @ id = "form-error-message"]')
    
    # Ссылка "Забыли пароль?"
    FORGOT = (By.CSS_SELECTOR, "#forgot_password")
    
    # Заголовок страницы справа
    PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    
    # Кнопка "Назад"
    BACK_BUTTON = (By.XPATH, '//*[@id="reset-back"]')
    
    # Кнопка "Регистрация"
    REGISTER = (By.XPATH, '// *[ @ id = "kc-register"]')
    
    # Поле для ввода имени
    NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    
    # Поле для ввода фамилии
    SURNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    
    # Поле для ввода региона
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    
    # Поле для ввода электронной почты
    EMAIL = (By.XPATH, '//*[@id="address"]')
    
    # Поле для ввода пароля при регистрации
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    
    # Поле для повторного ввода пароля при регистрации
    PASSWORD_REPEAT = (By.XPATH, '//*[@id="password-confirm"]')
    
    # Кнопка "Зарегистрироваться"
    BUTTON_REGISTER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    
    # Сообщение об ошибке для электронной почты
    ERROR_HINT_EMAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/div')
    
    # Сообщение об ошибке для имени
    ERROR_HINT_NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
    
    # Кнопка "ОК"
    OK = (By.CSS_SELECTOR, '#oidc_ok>svg')
    
    # Метка "ОК"
    LABLE_OK = (By.CSS_SELECTOR, '#widget-el>div.ext-widget_h>div')
    
    # Вкладка "Мой Мир"
    MY_WORLD = (By.XPATH, '//*[@id="oidc_mail"]')
    
    # Кнопка "Войти" на вкладке "Мой Мир"
    BUTTON_ENTRY_MM = (By.XPATH, '//*[@id="login-form"]/div[2]/button')
    
    # Вкладка "Яндекс"
    YA = (By.XPATH, '//*[@id="oidc_ya"]')
    
    # Метка "Яндекс"
    LABLE_YA = (By.ID, 'oidc_ya')
