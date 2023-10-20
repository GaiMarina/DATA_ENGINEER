"""Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между между переданными индексами.
Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.
"""

"""
def sum_between_indices(n_list: [int], ind_1: int, ind_2: int):
    if ind_1 > ind_2:
        ind_2, ind_1 = ind_1, ind_2
    nums_list = []

    if ind_1 not in range(0, len(n_list)):
        nums_list.extend([n_list[i] for i in range(ind_2)])
        print(nums_list)
        return sum(nums_list)

    elif ind_2 not in range(0, len(n_list)):
        nums_list.extend([n_list[i] for i in range(ind_1 + 1, len(n_list))])
        print(nums_list)
        return sum(nums_list)

    else:
        nums_list.extend([n_list[ind_1 + i] for i in range(1, ind_2 - 2)])
        print(nums_list)
        return sum(nums_list)


numbers = [82, 90, 23, 20, 85, 36, 37, 50, 4, 59, 6]
index_1, index_2 = map(int, input('Введите два индекса через пробел: ').split())
print(sum_between_indices(numbers, index_1, index_2))
"""
# =============================================

import random


def f1(l_1, idx1, idx2):
    return sum(l_1[idx1 + 1 if idx1 >= 0 else 0: idx2 if idx2 < len(l_1) else len(l_1)])


numbers_count = 10
numbers = [random.randint(0, 50) for _ in range(numbers_count)]
print(numbers)
print(f1(numbers, 7, 74))
