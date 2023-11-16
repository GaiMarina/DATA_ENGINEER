# -*- coding: cp1251 -*-

"""Напишите функцию, которая в бесконечном цикле запрашивает имя,
личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
from pathlib import Path
import json
import os

DATA_FILE = 'access_level.json'
DATA = {}
JSON_DIRECTION = '\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks'


def access_level():
    global DATA
    id_set = set()
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            DATA = json.load(f)
            for i in DATA.values():
                for j in i.keys():
                    id_set.add(j)
    # print(id_set)
    while True:
        action = input('Чтобы выйти, нажмите q, чтобы продолжить, нажмите любой другой символ: ')
        if action == 'q':
            quit('Bye!')
        else:
            pass
        draft_dict = {}
        name = input('Введите имя: ')
        while True:
            personal_id = input('Введите личный идентификатор: ')
            if personal_id in id_set:
                print('Данный идентификатор уже существует.')
                continue
            else:
                id_set.add(personal_id)
                # print(id_set)
                break
        while True:
            acc_level = input('Введите уровень доступа от 1 до 7: ')
            if acc_level in ['1', '2', '3', '4', '5', '6', '7']:
                break
            else:
                print('Неправильный ввод уровня доступа.')
                continue

        draft_dict[personal_id] = name
        DATA.setdefault(acc_level, {}).update(draft_dict)
        sorted_dict = dict(sorted(DATA.items(), key=lambda item: item[0]))
        json_data = json.dumps(sorted_dict, indent=2, ensure_ascii=False)
        os.chdir(JSON_DIRECTION)
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            f.write(json_data)


# print(access_level())

