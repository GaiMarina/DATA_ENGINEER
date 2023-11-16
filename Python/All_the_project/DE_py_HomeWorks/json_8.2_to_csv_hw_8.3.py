# -*- coding: cp1251 -*-
"""Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
"""

import csv
import json
import os

DATA_FILE = 'access_level.json'
CSV_DIRECTION = '\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks'


def json_to_csv():
    os.chdir(CSV_DIRECTION)
    with (open(DATA_FILE, 'r', newline='', encoding='utf-8') as json_file,
          open('csv_access_level.csv', 'w', newline='', encoding='utf-8') as csv_file
          ):
        data = json.load(json_file)

        csv_write = csv.DictWriter(csv_file, fieldnames=["access_level", "id", "name"],
                                   dialect='excel', quoting=csv.QUOTE_ALL)
        csv_write.writeheader()  # "access_level","id","name"
        access_level = []
        identifier = []
        names = []
        for key, value in data.items():
            # print(key, value)   # 1 {'1': 'Марина', '2': 'Оксана'}
            for k, v in value.items():
                access_level.append(key)
                identifier.append(k)
                names.append(v)

        dict_row = {}
        for i, j, k in zip(access_level, identifier, names):
            dict_row['access_level'] = i
            dict_row['id'] = j
            dict_row['name'] = k
            csv_write.writerow(dict_row)


json_to_csv()
