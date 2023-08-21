Окружение: Windows 10 Версия 115.0.5790.171 (Официальная сборка), (64 бит)

Для запуска тестов:

1. pip install -r requirements.txt

2. Скачать вебдрайвер Chrome с сайта https://chromedriver.chromium.org/

3. Выполнить запуск через команду python -m pytest -v tests/test.py. 


Файлы проекта: 

Корневой каталог:
config.py - содержит переменные используемые в проекте;
README.md - содержит информацию в целом о проекте;
requirements.txt - содержит все библиотеки и зависимости проекта

Директория tests:
conftest.py - условия для запуска браузера
test.py - автотесты по проекту
chromedricer.exe - файл драйвера для хром версии 115.0.5790.171

Директория pages:
Base_page.py - основные методы работы со страницей
Main_page.py - локаторы по проекту

→ Требования по проекту https://docs.google.com/document/d/1EWzdempFEOzzNnDM9YgcN2akToniXR03RgFhNEzf8IQ/edit?usp=sharing

→ Объект тестирования: https://b2c.passport.rt.ru

По проекту выполнены тест-кейсы и описаны возможные баги. 
https://docs.google.com/spreadsheets/d/1yo21yx8SVAK5HI-1ymsv3VK3cs1mpeT-6nxusBwmjQw/edit#gid=1908248823

 

Ответы на задание:

- Разработано 20 тест-кейсов
- Написано 20 автотестов (по одному автотесту на каждый написанный тест-кейс)


Техники тест-дизайна используемые в проекте:
    
1. Эквивалентное разбиение 
2. Предугадывание ошибок 
3. Анализ граничных значений 

В тестировании применены инструменты:

Google Docs - для составления тест-кейсов

ПО Pycharm - для написания и запуска автотестов

ПО Google Chrome - для запуска автотестов

Для запуска тестов необходимо установить все библиотеки, указанные в файле requirements.txt, скачать соответсвующий вышему окружению вебдрайвер для Chrome с сайта https://chromedriver.chromium.org/ и выполнить запуск через команду python -m pytest -v tests/test.py. 
В проекте использована версия драйвера 115.0.5790.171. Проект выполнен на Windows10 Chrome 115.0.5790.171 (Официальная сборка), (64 бит)

Для запуска определенного теста можно использовать: 

test - 1. python -m  pytest -v tests/test.py::test_main_logo
test - 2. python -m  pytest -v tests/test.py::test_invalid_auth_mail
test - 3. python -m  pytest -v tests/test.py::test_invalid_auth_mail
test - 4. python -m  pytest -v tests/test.py::test_pass_invalid_auth_parol
test - 5. python -m  pytest -v tests/test.py::test_pass_invalid_auth_mail
test - 6. python -m  pytest -v tests/test.py::test_pass_invalid_auth_mail
test - 7. python -m  pytest -v tests/test.py::test_forgot_password
test - 8. python -m  pytest -v tests/test.py::test_back_button
test - 9. python -m  pytest -v tests/test.py::test_click_check_in
test - 10. python -m  pytest -v tests/test.py::test_check_in
test - 11. python -m  pytest -v tests/test.py::test_check_in_false_email
test - 12. python -m  pytest -v tests/test.py::test_check_in_false_mobile_max
test - 13. python -m  pytest -v tests/test.py::test_check_in_false_mobile_mini
test - 14. python -m  pytest -v tests/test.py::test_check_in_false_name_mini
test - 15. python -m  pytest -v tests/test.py::test_check_in_name_two_letters
test - 16. python -m  pytest -v tests/test.py::test_check_in_name_thirty_letters
test - 17. python -m  pytest -v tests/test.py::test_check_in_name_thirty_one_letters
test - 18. python -m  pytest -v tests/test.py::test_click_ok
test - 19. python -m  pytest -v tests/test.py::test_click_mail
test - 20. python -m  pytest -v tests/test.py::test_click_ya
