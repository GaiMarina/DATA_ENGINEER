"""Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

Сортировка пузырьком — один из самых известных алгоритмов сортировки.
Здесь нужно последовательно сравнивать значения соседних элементов и менять числа местами,
если предыдущее оказывается больше последующего.
Таким образом элементы с большими значениями оказываются в конце списка, а с меньшими остаются в начале.
"""

import random

# nums_list = list(map(int, input('Введите несколько чисел через пробел: ').split()))
NUM = 10
LIMIT = 100
nums_list = [random.randint(1, LIMIT) for _ in range(NUM)]
print(nums_list)


def bubble_sort(n_lst: list[int]) -> list[int]:
    for i in range(len(n_lst)):
        for j in range(len(n_lst)):
            if n_lst[i] < n_lst[j]:
                n_lst[i], n_lst[j] = n_lst[j], n_lst[i]
    return n_lst


print(bubble_sort(nums_list))

#===================
"""
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


numbers = [82, 90, 23, 20, 85, 36, 37, 50, 4, 59]
print(numbers)
bubble_sort(numbers)
print(numbers)
"""

