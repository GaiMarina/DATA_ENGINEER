"""Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fibonacci_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for num in fibonacci_generator(10):
    print(num)
