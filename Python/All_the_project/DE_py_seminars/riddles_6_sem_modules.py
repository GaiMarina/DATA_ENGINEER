"""Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число
(номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.

"""

import random

# Ф-я для формирования словаря с инф-цией о результатах отгадвания.

_result_dict = {}
MAX_ATTEMPTS = 3

def dictionary_output(dic: dict):
    dic_out = {key: value for key, value in dic.items()}
    yield dic_out.items()


def dict_making(text: str, num: int):
    key = _result_dict.setdefault(text, list())
    key.append(num)
    return _result_dict


# Ф-я с загадками

def riddles_dict():
    riddles = [
        ["Висит груша, нельзя скушать", "груша"],
        ["Что может быть больше, чем Бог, огромнее мира, выше гор и глубже моря?", "ничто"],
        ["Кто его носит на спине, тот не видит его, а кто видит его, тот не носит его на спине?", "тень"],
        ["Что всегда идет вверх, но никогда не спускается вниз?", "возраст"],
        ["Что не может быть съедено, но может быть проглочено?", "воздух"],
        ["Какой зверь не может ходить по земле, но может плавать в воде?", "кит"]]

    dictionary = {}
    for line in riddles:
        guesses = ["груша", "ничто", "тень", "возраст", "воздух", "кит"]
        key = dictionary.setdefault(line[0], list())
        guesses.append(line[1])
        key.extend(guesses)
    items = list(dictionary.items())
    # Перемешиваем список кортежей
    random.shuffle(items)
    # Создаем новый словарь из перемешанного списка кортежей
    shuffled_dict = dict(items)
    for key, values in shuffled_dict.items():
        draft_dict = dict_making(key, puzzle_riddles(key, values, MAX_ATTEMPTS))
        for record in next(dictionary_output(draft_dict)):
            print(f'Загадка "{record[0]}"  разгадана! С {record[1][0]} раза.\n') if int(record[1][0]) > 0 else \
                print(f'Загадка "{record[0]}" за {MAX_ATTEMPTS} попытки не разгадана!\n')



# загадывающая фунукция
def puzzle_riddles(riddle: str, guess_list: list[str], max_attempts=3) -> int:
    count = 0
    while count < max_attempts:
        count += 1
        print(f'Попытка №{count}')
        clue = set(guess_list)
        clue = ', '.join(clue)
        attempts = input(f'Отгадайте загадку: {riddle}\nПодсказка: {clue}\n')

        guess_word = [word for word in guess_list if guess_list.count(word) == 2]
        if attempts.lower() == guess_word[0]:
            print(f'Правильно! С {count} попытки!')
            return count
        else:
            continue
    print('Сожалею, все попытки закончились. Попробуйте еще!\n')
    return 0


if __name__ == '__main__':
    print(riddles_dict())
