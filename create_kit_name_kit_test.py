import sender_stand_request
import data

# Функция для получения токена
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token


# Функция, меняющая содержимое тела запроса
def get_kit_body(name):
    # копирование в переменную current_body словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_kit_body = data.kit_body.copy()
    # изменение значения ключа на переменную name
    current_kit_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_kit_body


# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновлённое тело запроса:
    kit_body = get_kit_body(name)
    # Передаётся auth_token
    auth_token = get_new_user_token()
    # В переменную kit_responce сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа = 201
    assert kit_response.status_code == 201
    # Проверяется, что имя в наборе соответствует заданному
    assert kit_response.json()["name"] == name


 # Функция для негативной проверки
def negative_assert_code_400(name):
    # В переменную kit_body сохраняется обновлённое тело запроса:
    kit_body = get_kit_body(name)
    # Передаётся auth_token
    auth_token = get_new_user_token()
    # В переменную response сохраняется результат
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    #  Проверяется, что код ответа = 400
    assert kit_response.status_code == 400

# Тест 1. Допустимое количество символов
#  Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_kit_name_get_success_response():
    positive_assert("a")
# Тест 2. Допустимое количество символов
#  Параметр name состоит из 511  символа
def test_create_kit_511_letters_in_kit_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
# Тест 3. Ошибка. Количество символов меньше допустимого
# Параметр name не передан
def test_create_kit_0_letter_in_kit_name_get_error_response():
    negative_assert_code_400("")
# Тест 4. Ошибка. Количество символов в name больше допустимого
# Параметр name состоит из 512  символа
def test_create_kit_512_letters_in_kit_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
# Тест 5. Разрешены английские буквы
# Параметр name состоит из английских букв
def test_create_kit_english_letters_in_kit_name_get_success_response():
    positive_assert("QWErty")
# Тест 6. Разрешены русские буквы
# Параметр name состоит из русских букв
def test_create_kit_russian_letters_in_kit_name_get_success_response():
    positive_assert("Мария")
# Тест 7. Разрешены спецсимволы
# Параметр name состоит из спецсимволы
def test_create_kit_special_symbols_in_kit_name_get_success_response():
    positive_assert("\"№%@\",")
# Тест 8. Разрешены пробелы
# В параметре name есть пробелы
def test_create_kit_spaces_in_kit_name_get_success_response():
    positive_assert(" Человек и КО ")
# Тест 9. Разрешены цифры
# Параметр name состоит из цифр
def test_create_kit_numbers_in_kit_name_get_success_response():
    positive_assert("123")
# Тест 10. Ошибка. Параметр name не передан в запросе
def test_create_kit_empty_in_kit_name_get_error_response():
    negative_assert_code_400("")
# Тест 11. Ошибка. Передан другой тип параметра
# Параметр name состоит из number type
def test_create_kit_type_number_in_kit_name_get_error_response():
    negative_assert_code_400(123)
