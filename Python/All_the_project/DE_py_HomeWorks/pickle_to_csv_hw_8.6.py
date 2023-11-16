# -*- coding: cp1251 -*-
"""Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
"""
import pickle
import csv

PICKLE_FILE = '\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\json_hash_add_file.pickle'
CSV_FILE = '\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\json_hash_add_file.csv'


def pickle_to_csv(dir: str):
    with (open(PICKLE_FILE, 'rb') as pf,
          open(CSV_FILE, 'w', encoding='utf-8', newline='') as csvf
          ):
        data = pickle.load(pf)
        fildnames_list = list(data[0].keys())
        csv_write = csv.DictWriter(csvf, fieldnames=fildnames_list,
                                   dialect='excel',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        for dictionary in data:
            csv_write.writerow(dictionary)


pickle_to_csv(PICKLE_FILE)
