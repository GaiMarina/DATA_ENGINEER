print(f'\n1.\nСоздайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY \n'
      f'Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. \n'
      f'Для простоты договоримся, что год может быть в диапазоне [1, 9999]. \n'
      f'Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. \n'
      f'Проверку года на високосность вынести в отдельную защищённую функцию. \n')
print(f'В модуль с проверкой даты добавьте возможность запуска в терминале с передачей \n'
      f'даты на проверку.\n')


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
        print('Такой даты нет.')

print(
    f'----------------------------------------------------------------------------------------------------------------------')

print(f'Напишите функцию в шахматный модуль. \n'
      f'Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. \n'
      f'Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.  \n\n'

      f'Добавьте в пакет, созданный на семинаре, шахматный модуль. \n'
      f'Внутри него напишите код, решающий задачу о 8 ферзях. \n'
      f'Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. \n'
      f'Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. \n'
      f'Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. \n'
      f'Если ферзи не бьют друг друга верните истину, а если бьют - ложь. \n')

import random


# Список списков: 8 пар координат для расстановки ферзей.
def arrangement():
    all_the_lst = []
    while len(all_the_lst) < 8:
        # print(all_the_tuple)
        i = random.randint(1, 8)
        j = random.randint(1, 8)
        two = [i, j]
        # print(tup)
        if two not in all_the_lst:
            all_the_lst += [two]
        lines = []
        columns = []
        for pair in all_the_lst:
            i, j = pair
            lines.append(i)
            columns.append(j)
        if len(set(lines)) != len(lines) or len(set(columns)) != len(columns):
            all_the_lst.pop()
            continue
    yield all_the_lst  # [[2, 6], [3, 2], [4, 7], [7, 8], [8, 4], [8, 2], [6, 7], [6, 5]]


# Вывод True или False: является подходящим сочетанием или нет.
def queen_beats_checking(lst: list[list]):
    for two in lst:
        #  # левая верхняя диагональ
        a, b = two
        i = a
        j = b
        gen = ([i, j] for i, j in zip(range(i - 1, 0, -1), range(j - 1, 0, -1)))
        for x, y in gen:
            if [x, y] in lst:
                return False
        # правая нижняя диагональ
        i = a
        j = b
        gen = ([i, j] for i, j in zip(range(i + 1, 9), range(j + 1, 9)))
        for x, y in gen:
            if [x, y] in lst:
                return False
        # правая верхняя диагональ
        i = a
        j = b
        gen = ([i, j] for i, j in zip(range(i - 1, 0, -1), range(j + 1, 9)))
        for x, y in gen:
            if [x, y] in lst:
                return False
        # Проверяем правую нижнюю диагональ
        i = a
        j = b
        gen = ([i, j] for i, j in zip(range(i + 1, 9), range(j - 1, 0, -1)))
        for x, y in gen:
            if [x, y] in lst:
                return False
    return True


def chess_board(lst: list[list], num=8):
    # Создаем шахматную доску и размещаем ферзей в соответствии с координатами
    board = [[' ::' for _ in range(num)] for _ in range(num)]

    for coord in lst:
        x, y = coord
        board[x - 1][y - 1] = ' ' + chr(9813)

    # Выводим шахматную доску с ферзями
    for row in board:
        print(' '.join(row))
    return '\n\n'


# Вывод указанного значения работающих комбинаций.
def winner_num_combinations(num: int):
    win_combinations = []
    while True:
        ar = next(arrangement())
        if queen_beats_checking(ar):
            win_combinations.append(ar)
        if len(win_combinations) == num:
            return win_combinations


if __name__ == '__main__':
    for choice in winner_num_combinations(4):
        print(choice)
        print(chess_board(choice))
