# -*- coding: cp1251 -*-
"""Напишите функцию, которая ищет json файлы в указанной директории
и сохраняет их содержимое в виде одноимённых pickle файлов.
"""
import pickle
import os
import json

GIVEN_DIRECTION = '\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks'
EXTENSION = '.json'


def search_dir_by_extension_to_pickle(ext: str, direction: str):
    files_list = find_files_by_extension(ext, direction)
    for file in files_list:
        pickle_file, _ = file.split('.')
        pickle_file = pickle_file.split('\\')[-1]
        pickle_file += '.pickle'

        with (open(file, 'r', encoding='utf-8') as jf,
              open(pickle_file, 'wb') as pf
              ):
            os.chdir(GIVEN_DIRECTION)
            new_data = json.load(jf)
            res = pickle.dumps(new_data, protocol=pickle.DEFAULT_PROTOCOL)
            pf.write(res)


def find_files_by_extension(ext: str, dir):
    json_files = []

    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                json_files.append(os.path.join(root, file))

    return json_files


# search_dir_by_extension_to_pickle(EXTENSION, GIVEN_DIRECTION)
