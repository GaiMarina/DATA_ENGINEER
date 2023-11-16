import csv

# with open('biostats.csv', 'r', newline='') as f:        # newline убирает знаки конца строки

# csv_file = csv.reader(f) - позволяет построчно читать csv файл в список list

# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f)    # dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(line)
#     print(type(line))

# dialect='excel-tab' - разделитель табуляция (чтобы правильно считал)
# quoting=csv.QUOTE_NONNUMERIC) - если число не в кавычках, значит оно - число.

# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)      # ['Ruth', 'F', 28.0, 65.0, 131.0]
#     for line in csv_file:
#         print(line)


# --------------------------------------
# Запись в csv
# --------------------------------------

# csv_write = csv.writer(f)
# сохранять данные в формате csv

# csv_write.writerow(line)
# сохранение списка в одной строке файла в формате csv

# csv_write.writerows(all_data)
# сохранение матрицы в нескольких строках файла в формате csv (матрица - список списков)

# тоже на выходе - без запятых, без кавычек, но тоже csv-файл
# with (
#     open('biostats.csv', 'r', newline='') as f_read,
#     open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read = csv.reader(f_read, quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     all_data = []       # будет список списков: матрица
#     for i, line in enumerate(csv_read):
#         if i == 0:
#             csv_write.writerow(line)    # первая строка сразу идет в заголовок
#         else:
#             line[2] += 1  # то, что в ячейке 2 (возраст), увеличить на единицу
#             for j in range(2, 4 + 1):
#                 line[j] = int(line[j])
#             all_data.append(line)
#     csv_write.writerows(all_data)

# delimiter=' ' - объекты между собой надо разделять пробелами.
# quotechar='|' - если есть пробелы, такой объект экранируется чертой.
# quoting=csv.QUOTE_MINIMAL - использовать символы разделители только там, где это необходимо.
# (если есть пробел, возьмет в кавычки, а в данном случае вместо кавычек - черта.)

#-------------------------------------------
# Чтение csv в словарь
#-------------------------------------------

# csv_file = csv.DictReader(f, fieldnames=['name', 'sex', 'age', 'height', 'weight', 'office'],
#                           restkey='new', restval='Main Office')

# fieldnames - список заголовкой столбцов словаря
# restkey - значение ключа для столбцов, которых нет в fieldnames
# restval - значение поля для ключей fieldnames, которых нет в файле csv

# import csv

# поля office изначально нет => используем значение из restval - Main Office. ('office': 'Main Office')
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
#                               restkey="new", restval="Main Office", dialect='excel-tab',
#                               quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')

# то же самое, кроме строчек 4, 5.

# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age",],  # 'new': ['Height (in)', 'Weight (lbs)']
#                               restkey="new", restval="Main Office",
#                               quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#         print(f'{line["name"] = }\t{line["age"] = }')
# height, weight убрали => используем restkey 'new'

# ------------------------------------
# запись csv из словаря
# ------------------------------------

# csv_write.writeheader()
# сохранение первой строки с заголовками в порядке их перечисления в fieldnames
#
# csv_write.writerow(line)
# сохранение списка в одной строке файла в формате csv
#
# csv_write.writerows(all_data)
# cохранение матрицы в нескольких строках файла в формате csv

# import csv
# from typing import Iterator
#
# with(
#     open('biostats.csv', 'r', newline='') as f_read,
#     open('biostats_tab.csv', 'w', newline='', encoding='utf-8') as f_write
# ):
#     csv_read: Iterator[dict] = csv.DictReader(f_read,   # аннотация типов
#                                               fieldnames=["name", "sex", "age", "height", "weight", "office"],
#                                               restval="Main Office", quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.DictWriter(f_write, fieldnames=['id', 'name', 'office', 'sex', 'age', 'height', 'weight'],
#                                dialect='excel-tab', quoting=csv.QUOTE_ALL)
#     csv_write.writeheader() # запишет заголовки из 114-й строки именно в том порядке, как там.
#     all_data = []
#     for i, dict_row in enumerate(csv_read):
#         if i != 0:
#             dict_row['id'] = i
#             dict_row['age'] += 1
#             all_data.append(dict_row)
#     csv_write.writerows(all_data)
# поле id отсутствует в исходном файле и в словаре для чтения.
# quoting=csv.QUOTE_ALL - заключаем все в кавычки, не важно текст или числа.

# ----------------------------
# Task
# -------------------------

import csv

with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.DictWriter(f_write, fieldnames=["number", "name", "data"], restval='Hello World!',
                               dialect='excel', delimiter='#',
                               quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
    csv_write.writeheader()
    dict_row = {}
    for i in range(10):
        dict_row['number'] = i
        dict_row['name'] = str(i)
        csv_write.writerow(dict_row)
