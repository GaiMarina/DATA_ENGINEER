"""Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
- расширение
- минимальная длина случайно сгенерированного имени, по умолчанию 6
- максимальная длина случайно сгенерированного имени, по умолчанию 30
- минимальное число случайных байт, записанных в файл, по умолчанию 256
- максимальное число случайных байт, записанных в файл, по умолчанию 4096
- количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
"""

from pseudonyms_generator import pseudonyms_gen
from random import randint, choice
import os


# Функция сохраняет в текущую директорию
def files_generator(ext: str, min_name=6, max_name=30, min_bytes=256, max_bites=4096, files_num=42):
    count = 0
    while count < files_num:
        name = pseudonyms_gen(min_len=min_name, max_len=max_name)
        name += ext
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, name)
        open(file_path, 'x', encoding='utf-8')
        # открываем файл для записи в бинарном режиме
        num_bytes = randint(min_bytes, max_bites)
        with open(file_path, "wb+") as f:
            # генерируем случайные байты и записываем их в файл
            for i in range(num_bytes):
                # генерируем случайный байт от 0 до 255
                byte = randint(0, 255)
                # преобразуем число в байтовую строку и записываем в файл
                f.write(byte.to_bytes(1, "big"))  # от старшего к младшему

        count += 1
    else:
        return 'fin'


# print(files_generator('.txt', files_num=3))
#
# print(os.path.getsize('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute\\Jscspmbpzoypna.txt'))
"""
Доработаем предыдущую задачу.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""


def dif_extention_files(ext_list: [str], count: int):
    counter = 0
    while counter < count:
        extension = choice(ext_list)
        files_generator(extension, files_num=1)
        counter += 1
    else:
        return 'fin'


# extension_lst = ['.docx', '.gif', 'txt']
# dif_extention_files(extension_lst, 5)
"""
Дорабатываем функции из предыдущих задач.
Генерируйте файлы в указанную директорию — отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


# сохраняет файлы в указанную директорию
def files_gen_to_dir(ext: str, file_path: str, min_name=6, max_name=30, min_bytes=256, max_bites=4096, files_num=42):
    global file
    count = 0
    if not os.path.isdir(file_path):
        print('Данной директории не существует')
        quit()
    while count < files_num:
        name = pseudonyms_gen(min_len=min_name, max_len=max_name)
        name += ext
        file_path = os.path.join(file_path, name)
        num_bytes = randint(min_bytes, max_bites)
        try:
            open(file_path, 'x', encoding='utf-8')
        except FileExistsError:
            print(f'Файл {file_path} уже существует.')
            continue
        finally:
            with open(file_path, "wb+") as f:
                # генерируем случайные байты и записываем их в файл
                for i in range(num_bytes):
                    # генерируем случайный байт от 0 до 255
                    byte = randint(0, 255)
                    # преобразуем число в байтовую строку и записываем в файл
                    f.write(byte.to_bytes(1, "big"))  # от старшего к младшему
        count += 1
        continue
    else:
        return 'fin'


def dif_extention_files_to_dir(ext_list: [str], count: int, file_path: str):
    counter = 0
    while counter < count:
        extension = choice(ext_list)
        files_gen_to_dir(extension, file_path, files_num=1)
        counter += 1
    else:
        return 'fin'


extension_lst = ['.docx', '.gif', '.txt']
f_path = '\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute'
dif_extention_files_to_dir(extension_lst, 5, f_path)
