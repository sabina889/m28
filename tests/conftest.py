import pytest
from selenium import webdriver

# Импорт необходимых модулей

# Декоратор @pytest.fixture
@pytest.fixture
def driver():
    # Настройка и создание WebDriver перед выполнением тестов

    # Инициализация драйвера Chrome
    driver = webdriver.Chrome('chromedriver.exe')
    
    # Максимизация окна браузера
    driver.maximize_window()
    
    # Установка неявного ожидания (Implicit Wait) в 10 секунд
    driver.implicitly_wait(10)
    
    # Возврат драйвера, чтобы его можно было использовать в тестах
    yield driver
    
    # Завершение работы драйвера после выполнения тестов
    driver.quit()
