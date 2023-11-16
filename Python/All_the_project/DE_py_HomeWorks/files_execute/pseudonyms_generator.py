"""Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""
from random import randint, choice


def pseudonyms_gen(min_len, max_len):
    vowel_letters = set('aeiouy')
    name_len = randint(min_len, max_len)
    name = [chr(randint(ord('a'), ord('z'))) for _ in range(name_len)]
    if len(vowel_letters.intersection(set(name))) == 0:
        name[randint(0, len(name) - 1)] = choice(list(vowel_letters))
    name = ''.join(name).capitalize()
    return name


if __name__ == '__main__':
    MIN_ORD = ord('a')
    MAX_ORD = ord('z')
    MIN_LEN = 4
    MAX_LEN = 7
    file_name = 'pseudonyms_generator.txt'
    m = 10
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(m):
            f.write(f'{pseudonyms_gen(MIN_LEN, MAX_LEN)}\n')
