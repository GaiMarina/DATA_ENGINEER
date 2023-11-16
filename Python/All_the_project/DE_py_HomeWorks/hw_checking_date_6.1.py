"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

"""Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""


from datetime import date
from time import strptime
import sys


def is_valid_date(date_string, date_format="%d.%m.%Y"):
    try:
        strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def checking_date(input_date: date | str) -> bool:
    if is_valid_date(my_date):
        return True
    else:
        return False


def _gregorian_checking(input_date: date) -> bool:
    if is_valid_date(input_date):
        input_year = int(input_date[-4:])
        if input_year < 1582:
            print(f'Ошибка! Неправильный ввод')
        elif input_year % 400 == 0 or (input_year % 4 == 0 and input_year % 100 != 0):
            return True  # високосный
        else:
            return False


if __name__ == "__main__":
    try:
        my_date = sys.argv[1]
    except:
        my_date = input('Введите дату в формате DD.MM.YYYY: ')

    if checking_date(my_date):
        print(f'Дата {my_date} существует')
    else:
        print('Такой даты нет')

# python DE_py_HomeWorks\\hw_checking_date_6.1.py 01.12.2002
