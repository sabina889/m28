# Корректные данные для тестов
valid_email = "babaevaO8O8@mail.ru"
valid_pass = "Sabina88989"

# Некорректные данные для тестов
invalid_email = 'babaуevaO8O8@mail.ru'
invalid_pass = 'Sabina88у989'

# Личная информация пользователя
name = 'Сабина'
surname = 'Бабаева'
region = 'Ульяновская обл'
email = 'babaeva0808@mail.ru'
password = 'Sabina88989'

# Некорректные данные разных типов
false_email = '345678'
false_mobile_max = '891275643437'
false_mobile_mini = '8953785652'
false_name_mini = 'B'
name_two_letters = "Ау"
thirty_letters = 'Вецезиабобонпгкзарордоенеопрнь'
thirty_one_letters = 'Вецезиабобонпгкзарордоенеопрньк'

# Класс с тестовыми данными и строками для интерфейса
class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    # Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'E-mail или мобильный телефон'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Продолжить'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
