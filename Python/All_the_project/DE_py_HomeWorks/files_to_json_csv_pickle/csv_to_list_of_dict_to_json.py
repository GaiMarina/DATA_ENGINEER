# -*- coding: cp1251 -*-
"""Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы функции.
"""

import csv
import hashlib
import os
import json

CSV_DIRECTION = '\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks'
ORIGINAL = 'csv_access_level.csv'
JSON_FILE = 'json_hash_add_file.json'
JSON_LIST = list()


def csv_to_json(original, json_file):
    os.chdir(CSV_DIRECTION)
    with (open(original, 'r', newline='', encoding='utf-8') as csv_file,
          open(json_file, 'w', encoding='utf-8') as json_f
          ):
        csv_read = csv.reader(csv_file, dialect='excel', quoting=csv.QUOTE_ALL)
        for i, line in enumerate(csv_read):  # 0 ['access_level', 'id', 'name'] 1 ['1', '1', 'Марина']
            if i == 0:
                header = line
                header.append('hash')
                continue
            line[1] = line[1].zfill(10)
            line[2] = line[2].capitalize()
            data = line[2] + line[1]
            hashed = hashlib.md5(data.encode()).hexdigest()  # md5 - хэш-функциz из библиотеки hashlib
            line.insert(3, hashed)
            for _ in range(len(line) + 1):
                draft_dict = {}
                for h, v in zip(header, line):
                    draft_dict[h] = v
            JSON_LIST.append(draft_dict)
        json.dump(JSON_LIST, json_f, indent=2, ensure_ascii=False)


# csv_to_json(ORIGINAL, JSON_FILE)
