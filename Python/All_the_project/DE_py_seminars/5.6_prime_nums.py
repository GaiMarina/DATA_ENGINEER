"""Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: «число является простым,
если делится нацело только на единицу и на себя».

"""
import itertools


def prime_nums_generator(n: int):
    count = 0
    number = 2
    while count < n:
        if all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
            yield number
            count += 1
        number += 1


for prime in prime_nums_generator(10):
    print(prime)
