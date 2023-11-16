# -*- coding: cp1251 -*-
"""�������� �������, ������� ����������� pickle ���� �������� ������ �������� � ��������� csv ����.
��� ������������ �������� pickle ������ ����� �� ������ 4 ����� ��������.
������� ������ ��������� ����� ������� ��� ���������� ������� �� ����������� �����.
"""
import pickle
import csv

PICKLE_FILE = '\\Users\\��\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\json_hash_add_file.pickle'
CSV_FILE = '\\Users\\��\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\json_hash_add_file.csv'


def pickle_to_csv(dir: str, csv_file):
    with (open(dir, 'rb') as pf,
          open(csv_file, 'w', encoding='utf-8', newline='') as csvf
          ):
        data = pickle.load(pf)
        fildnames_list = list(data[0].keys())
        csv_write = csv.DictWriter(csvf, fieldnames=fildnames_list,
                                   dialect='excel',
                                   quoting=csv.QUOTE_ALL)
        csv_write.writeheader()
        for dictionary in data:
            csv_write.writerow(dictionary)


# pickle_to_csv(PICKLE_FILE, CSV_FILE)
