
"""Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака."""


# Выведет указанное количество вариантов. Лучше в пределах 5, а то ему трудно)

import random

BACKPACK_CARRYING_CAPACITY = 8
MIN_CAPACITY = 7

backpack_things = {
    'Палатка': 3.5,
    'Спальный мешок': 2.2,
    'Коврик для сна': 0.8,
    'Котелок': 1.7,
    'Топор': 1.5,
    'Фонарик': 0.4,
    'Переносная плита': 2.9,
    'Нож': 0.2,
    'Аптечка': 0.6,
    'Питьевая система': 1.0
}

VARIANTS_NUMBER = int(input('Введите необходимое количество вариантов: '))
backpack_variants = {}

while len(backpack_variants) < VARIANTS_NUMBER:
    dict_keys = list(backpack_things.keys())
    random.shuffle(dict_keys)
    shuffled_keys = dict_keys
    f = True
    while f:
        weight = sum(backpack_things[key] for key in shuffled_keys)
        if weight > BACKPACK_CARRYING_CAPACITY:
            shuffled_keys.pop()
            continue
        elif weight < BACKPACK_CARRYING_CAPACITY:
            sorted_keys = tuple(sorted(shuffled_keys))
            if sorted_keys in backpack_variants:
                f = False
            else:
                backpack_variants[tuple(sorted(shuffled_keys))] = round(weight, 1)
                f = False
        else:
            continue
n = 0
for things, weight in backpack_variants.items():
    n += 1
    print(f'{n:<4} {weight:<3} кг.: {things}')

# ==========================
"""
# Все возможные варианты


import itertools


BACKPACK_CARRYING_CAPACITY = 8
MIN_CAPACITY = 7

backpack_things = {
    'Палатка': 3.5,
    'Спальный мешок': 2.2,
    'Коврик для сна': 0.8,
    'Котелок': 1.7,
    'Топор': 1.5,
    'Фонарик': 0.4,
    'Переносная плита': 2.9,
    'Нож': 0.2,
    'Аптечка': 0.6,
    'Питьевая система': 1.0
}


def find_combinations(dictionary: dict, target_sum: int, min_sum: int) -> dict:
    keys = list(dictionary.keys())
    combinations = dict()

    for r in range(1, len(keys) + 1):
        for combination in itertools.combinations(keys, r):                     # itertools.combinations(
            values_sum = round(sum(dictionary[key] for key in combination), 1)  # итератор, размер каждой комбинации)
            if target_sum >= values_sum > min_sum:
                combinations[combination] = values_sum
    return combinations

    # return f'sorted(combinations.items(), key=len, reverse=True)


possible_variants = find_combinations(backpack_things, BACKPACK_CARRYING_CAPACITY, MIN_CAPACITY)
# print(len(possible_variants)) # 132

counter = 0
for things, weight in sorted(possible_variants.items(), key=lambda x: len(x[0]), reverse=True):
    counter += 1
    print(f'{counter:<4} {weight:<3} кг.: {things}')
"""