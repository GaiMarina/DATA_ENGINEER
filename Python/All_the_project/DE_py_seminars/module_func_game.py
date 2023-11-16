"""Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
import random

_LOWER_LIMIT = 0
_UPPER_LIMIT = 60
_TESTS_NUM = 3


def main():
    print(more_less_game(_LOWER_LIMIT, _UPPER_LIMIT, _TESTS_NUM))


def more_less_game(lower_limit=0, upper_limit=1_000, test_num=10):
    count = 1
    num = random.randint(lower_limit, upper_limit)
    while count <= test_num:
        while True:
            n = int(input(f'Угадайте число от {lower_limit} до {upper_limit} за {test_num} попыток. Попытка № {count}: '))
            if n < lower_limit or n > upper_limit:
                print('Я вас не понимаю. Попробуйте снова: ')
            else:
                break
        print('Вы ввели число ' + str(n))
        count += 1
        if n == num:
            # print('Вы молодец! Угадали!')
            return True
        else:
            print('Больше') if n < num else print('Меньше')

    # print(f'Исчерпаны все попытки. Сожалею.')
    print('Я загадал ' + str(num))
    return False


if __name__ == "__main__":
    print(main())
