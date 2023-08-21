# Для запуска всех тестов
# python -m pytest -v tests/test.py

from pages.Main_page import MainPage
from config import TestData, valid_pass, valid_email, invalid_pass, invalid_email, name, surname, region, email, \
    password, false_email, false_mobile_mini, false_mobile_max, false_name_mini, name_two_letters, \
    thirty_letters, thirty_one_letters

# test № 1
# Логотип Ростелеком (переход на страницу авторизации) виден на странице
# python -m  pytest -v tests/test.py::test_main_logo

def test_main_logo(driver):
    main_page = MainPage(driver)
    logo = main_page.is_visible(MainPage.MAIN_LOGO)
    assert logo == True # Тест успешно завершен (PASSED)
    

# test № 2
# Кнопка "Почта" кликабельна и открывает форму авторизации с полем "Электронная почта"
# python -m  pytest -v tests/test.py::test_mail_clickable

def test_mail_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIL)
    mail = main_page.is_visible(MainPage.USERNAME)
    assert mail == True # Тест успешно завершен (PASSED)

# test № 3

# Тест не прошел (FAILED)
# Авторизация по электронной почте и паролю
# python -m  pytest -v tests/test.py::test_auth_mail

def test_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    logout = main_page.is_visible(MainPage.BUTTON_LOGOUT)
    assert logout == True # Тест падает от капчи  (FAILED)

# test № 4
# python -m  pytest -v tests/test.py::test_invalid_auth_mail

def test_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, invalid_email)
    main_page.input_keys(MainPage.PASS, invalid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    assert error == True # Тест успешно завершен (PASSED)

# test № 5
# Авторизация по валидной электронной почте и невалидному паролю
# python -m  pytest -v tests/test.py::test_test_pass_invalid_auth_parol

def test_pass_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, valid_email)
    main_page.input_keys(MainPage.PASS, invalid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error_pass = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    assert error_pass == True # Тест успешно завершен (PASSED)

# test № 6
# Авторизация по невалидной электронной почте и валидному паролю
# python -m  pytest -v tests/test.py::test_pass_invalid_auth_mail

def test_pass_invalid_auth_mail(driver):
    main_page = MainPage(driver)
    main_page.input_keys(MainPage.USERNAME, invalid_email)
    main_page.input_keys(MainPage.PASS, valid_pass)
    main_page.find_click(MainPage.BUTTON_INPUT)
    error_username = main_page.is_visible(MainPage.ERROR_USERNAME_PASS)
    assert error_username == True # Тест успешно завершен (PASSED)

# test № 7
# Кнопка "Забыл пароль" кликабельна и открывает форму "Восстановление пароля"
# python -m  pytest -v tests/test.py::test_forgot_password

def test_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORGOT)
    recovery = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert recovery == TestData.RECOVERY # Тест успешно завершен (PASSED)

# test № 8
# Кнопка "Вернуться назад" в форме "Восстановление пароля" кликабельна и открывает форму "Авторизация"
# python -m  pytest -v tests/test.py::test_back_button

def test_back_button(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FORGOT)
    main_page.find_click(MainPage.BACK_BUTTON)
    auth_name = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert auth_name == TestData.AUTH # Тест успешно завершен (PASSED)

# test № 9
# Кнопка "Зарегистрироваться" кликабельна и открывает форму "Регистрация"
# python -m  pytest -v tests/test.py::test_click_check_in

def test_click_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    check_in = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert check_in == TestData.CHECK # Тест успешно завершен (PASSED)

# test № 10
# Заполнение формы "Регистрация" валидными данными и кликабельность кнопки "Зарегистрироваться"
# python -m  pytest -v tests/test.py::test_check_in

def test_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_reg == TestData.VERIFICATION_EMAIL # Тест успешно завершен (PASSED)

# test № 11
# Заполнение формы "Регистрация" c невалидным email
# python -m  pytest -v tests/test.py::test_check_in_false_email

def test_check_in_false_email(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == TestData.VERIFICATION_INVALID_EMAIL # Тест успешно завершен (PASSED)

# test № 12
# Заполнение формы "Регистрация" c невалидным mobile (на 1 цифру больше)
# python -m  pytest -v tests/test.py::test_check_in_false_mobile_max

def test_check_in_false_mobile_max(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_mobile_max)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == TestData.VERIFICATION_INVALID_EMAIL # Тест успешно завершен (PASSED)

# test № 13
# Заполнение формы "Регистрация" c невалидным mobile (на 1 цифру меньше)
# python -m  pytest -v tests/test.py::test_check_in_false_mobile_mini

def test_check_in_false_mobile_mini(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, false_mobile_mini)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_EMAIL)
    assert invalid_reg == TestData.VERIFICATION_INVALID_EMAIL # Тест успешно завершен (PASSED)

# test № 14
# Заполнение формы "Регистрация" с невалидным именем (менее 2 символов)
# python -m  pytest -v tests/test.py::test_check_in_false_name_mini

def test_check_in_false_name_mini(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, false_name_mini)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_NAME)
    assert invalid_reg == TestData.VERIFICATION_INVALID_NAME # Тест успешно завершен (PASSED)

# test № 15
# Заполнение формы "Регистрация" с валидным именем (2 кириллических символа)
# python -m  pytest -v tests/test.py::test_check_in_name_two_letters

def test_check_in_name_two_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, name_two_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_reg == TestData.VERIFICATION_EMAIL # Тест успешно завершен (PASSED)

# test № 16
# Заполнение формы "Регистрация" с валидным именем (30 кириллических символов)
# python -m  pytest -v tests/test.py::test_check_in_name_thirty_letters

def test_check_in_name_thirty_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, thirty_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    valid_reg = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_reg == TestData.VERIFICATION_EMAIL # Тест успешно завершен (PASSED)
 
# test № 17
# Заполнение формы "Регистрация" с невалидным именем (31 кириллический символ)
# python -m  pytest -v tests/test.py::test_check_in_name_thirty_one_letters

def test_check_in_name_thirty_one_letters(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.REGISTER)
    main_page.input_keys(MainPage.NAME, thirty_one_letters)
    main_page.input_keys(MainPage.SURNAME, surname)
    main_page.input_keys(MainPage.REGION, region)
    main_page.input_keys(MainPage.EMAIL, email)
    main_page.input_keys(MainPage.PASSWORD, password)
    main_page.input_keys(MainPage.PASSWORD_REPEAT, password)
    main_page.find_click(MainPage.BUTTON_REGISTER)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_HINT_NAME)
    assert invalid_reg == TestData.VERIFICATION_INVALID_NAME # Тест успешно завершен (PASSED)

# test № 18
# Кнопка "OK" кликабельна и открывает форму для регистрации через аккаунт OK
# python -m  pytest -v tests/test.py::test_click_ok

def test_click_ok(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OK)
    check_in = main_page.get_text_of_element(MainPage.LABLE_OK)
    assert check_in == TestData.OK # Тест успешно завершен (PASSED)

# test № 19
# Кнопка "@" ("Мой мир") кликабельна и открывает форму для регистрации через аккаунт Электронную почту
# python -m  pytest -v tests/test.py::test_click_mail

def test_click_mail(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MY_WORLD)
    check_in = main_page.get_text_of_element(MainPage.BUTTON_ENTRY_MM)
    assert check_in == TestData.MM # Тест успешно завершен (PASSED)

 # test №20
 # Кнопка "Я" кликабельна и открывает форму для регистрации через аккаунт Яндекс
 # python -m  pytest -v tests/test.py::test_click_ya

def test_click_ya(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.YA)
    check_in = main_page.is_visible(MainPage.LABLE_YA)
    assert check_in == True # Тест успешно завершен (PASSED)
