"""Создайте модуль с функцией внутри. 
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток. 
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток. 
Функция выводит подсказки “больше” и “меньше”. 
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""
"""Улучшаем задачу. 
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала. 
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции. 
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""
import sys
from module_func_game import more_less_game as game

# print(sys.argv)
# game(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
# python DE_py_seminars\\sem_modules_under_alias_6.1.py 10 50 3 (в терминале)
# название строки с командной строки - sys.argv
nums_list = list(map(int, [n for n in sys.argv[1:]]))

if len(nums_list) == 2:
    LOWER_LIMIT, UPPER_LIMIT = nums_list
    TESTS_NUM = 10
elif len(nums_list) == 1:
    LOWER_LIMIT = int(sys.argv[1])
    UPPER_LIMIT = 1_000
    TESTS_NUM = 10
else:
    LOWER_LIMIT, UPPER_LIMIT, TESTS_NUM, *_ = nums_list

print('Победа!!!') if game(LOWER_LIMIT, UPPER_LIMIT, TESTS_NUM) \
    else print('Сожалею. Больше попыток нет!')



