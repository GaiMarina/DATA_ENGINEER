# -*- coding: cp1251 -*-
"""�������� �������, ������� �������� �� ���� ���������� � ���������� ������� � � ��� ��������� ����������.
���������� ������ ��������� � ����� json, csv � pickle.
��� �������� �������� ���������� ������������ ����������.
��� ������� ������� ������� ���� ��� ��� ����������.
��� ������ ��������� ��� ������ � ������, � ��� ���������� ������ ������ � ��� � ������
���� ��������� ������ � ����������.
�������� �� ��������� �� ����� � � ������ ��������� ������� ������� �����  ��� ������ � ������� ������ ��������.
"""

import os
import json
import csv
import pickle

DIRECTION = "\\Users\\��\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project"
DATA = []
GIVEN_DIRECTION = '\\Users\\��\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks'


# �-� ����������� ������� ���������� ��� �����
def get_size(p_ath):
    total_size = 0
    for entry in os.scandir(p_ath):
        if entry.is_dir():
            total_size += get_size(entry.path)  # ������ ��������� ���������� � �������
        else:
            total_size += entry.stat().st_size  # ���������� ������� ������
    return total_size


def dir_list_of_dict(dir_path):
    DATA = []
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for dir in dirnames:
            dir_dict = {}
            dir_dict.update({'type': 'directory'})
            dir_dict.update({'name': dir})  # �������� �����
            dir_dict.update({'size': get_size(os.path.join(dirpath, dir))})  # ������ �����
            dir_dict.update({'parent_dir': dirpath})  # ������������ ����������
            DATA.append(dir_dict)
        for file in filenames:
            dir_dict = {}
            dir_dict.update({'type': 'file'})
            dir_dict.update({'name': file})
            dir_dict.update({'size': os.path.getsize(os.path.join(dirpath, file))})
            dir_dict.update({'parent_dir': os.path.join(dirpath, file)})  # ������������ ���������� ���������� �����
            DATA.append(dir_dict)

    return DATA


def list_of_dict_to_json(dict_list: [dict]):
    with open('directions_to_json.json', 'w', encoding='utf-8') as jf:
        os.chdir(GIVEN_DIRECTION)
        json.dump(dict_list, jf, indent=2, ensure_ascii=False)
    return 'fin'


def list_of_dict_to_csv(lst: [dict]):
    # ����� ��� ���������� csv
    keys = [key for key in lst[0].keys()]

    # ��������� csv ���� �� ������
    with open('directions_to_csv.csv', 'w', newline='', encoding='utf-8') as csvf:
        # ������� csv writer
        writer = csv.writer(csvf)
        # ���������� ��������� � ������ ��� csv �����
        writer.writerow(keys)
        # ���������� ������ � csv ����
        for d in lst:
            writer.writerow([d[key] for key in keys])
    return 'fin'


def list_of_dict_to_pickle(li_st: [dict]):
    with open('directions_to_pickle.pickle', 'wb') as file:
        pickle.dump(li_st, file)
    return 'fin'

# ������ ��������
# print(dir_list_of_dict(DIRECTION))

# to json
# list_of_dict_to_json(dir_list_of_dict(DIRECTION))

# to csv
# list_of_dict_to_csv(dir_list_of_dict(DIRECTION))

# to pickle
# list_of_dict_to_pickle(dir_list_of_dict(DIRECTION))

# ��������� pickle
# with open('directions_to_pickle.pickle', 'rb') as file:
#     list_of_dicts = pickle.load(file)
#
# print(list_of_dicts)
