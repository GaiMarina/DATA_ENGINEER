# -*- coding: cp1251 -*-
"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.
"""
import csv
import pickle

CSV_FILE = '\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\json_hash_add_file.csv'

with (
    open(CSV_FILE, 'r', newline='', encoding='utf-8') as f_read,
):
    csv_read = csv.reader(f_read, dialect='excel', quoting=csv.QUOTE_ALL)
    pickle_dumps = pickle.dumps(list(csv_read), protocol=pickle.DEFAULT_PROTOCOL)
    print(f'{pickle_dumps = }')
    # new_dict = pickle.loads(pickle_dumps)
    # print(f'{new_dict = }')