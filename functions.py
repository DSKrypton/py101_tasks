"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
import re
from keyword import iskeyword


def whether_not_all_odd_check(input_string):
    numbers_list = re.split(', |; | |,|;|\n', input_string)
    is_even_number_found = False
    for number in numbers_list:
        try:
            if int(number) % 2 == 0:
                is_even_number_found = True
        except ValueError:
            print(f'Something wrong, not an integer \'{number}\' detected among input')

    print('There is impostor(even number) among input' if is_even_number_found else 'All numbers are odd')


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
def sell_alcohol():
    print("Sold")


ALCOHOL_LEGAL_AGE = 21
age = 17
(print("Мы не продаём алкоголь несовершеннолетним.")) if age < ALCOHOL_LEGAL_AGE else sell_alcohol()


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def is_keyword(str):
    return iskeyword(str)


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."
def russian_object_type(obj):
    en_ru_type_translation = {
        "int": "целое число",
        "float": "число с плавающей точкой",
        "str": "строка",
        "bool": "булевый",
        "NoneType": "None",
        "list": "список",
        "tuple": "кортеж",
        "set": "множество",
        "dict": "словарь"
    }
    return f'Это {en_ru_type_translation[type(obj).__name__]}.'
