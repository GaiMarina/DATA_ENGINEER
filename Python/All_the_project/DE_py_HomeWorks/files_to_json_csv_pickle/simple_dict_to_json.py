# -*- coding: cp1251 -*-

"""���������� ������ 3 �� �������� ��������.
�� ������������ ��������� ���� � ������ ������� � ������������� �����.
�������� �������, ������� ������ �� ���������� ����� ����� ����� � ������� � ������� JSON.
����� ������ � ������� �����.
������ ���� ���������� � ����� ������.
"""

import os
import json

from pathlib import Path


def parse_and_create_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        my_dict = {}
        for line in f:
            res = line.strip().split(' | ')
            my_dict[res[0].capitalize()] = float(res[1])
        # print(my_dict)
        json_data = json.dumps(my_dict, indent=2, ensure_ascii=False)
        with open(output_file, 'w', encoding='utf-8') as jf:
            jf.write(json_data)


os.chdir('\\Users\\��\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute')
input = 'result.txt'
output = 'json_result.txt'

# parse_and_create_json(input, output)
