"""Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""
import random


def random_pairs(line_num: int, file_name: str):
    with open(file_name, 'a+', encoding='utf-8') as f:
        for _ in range(line_num):
            int_1, float_2 = random.randint(-1_000, 1_000), random.uniform(-1_000.0, 1_000.0)
            f.write(f'{int_1} | {float_2} \n')


print(random_pairs(4, 'num_pairs.txt'))
