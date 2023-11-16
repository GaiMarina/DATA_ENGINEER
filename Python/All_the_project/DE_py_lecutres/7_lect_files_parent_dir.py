# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
import glob
# f = open('text_data.txt') Если файл в той же папке можно коротко, а не весь путь.

# r  - чтение (по умолчанию)
# w - запись (перезаписывает то, что есть)
# x - если файл существует, вернет ошибку. Создаст только если нет файла для записи с нуля.
# a - дозапись того, что есть. В конец. (append)
# b - двоичный режим. (записываем не текст, а набор байт)
# t - пишем не бинарный текст, а текстовый. (по умолчанию
# + (r+, w+) дополнительно открыт и для чтения и для записи. Можно и то и др.
#   r+ не будет стирать файл, а w+ сначала сотрет, потом запишет.

# f.close() для гарантии сохранности данных файла.

# errors - В текстовом формате указываем как обрабатывать ошибки, которые могут возникать.

# ➢ 'strict' — вызывает исключение ValueError в случае ошибки. Работает как
# значение по умолчанию.
# ➢ 'ignore' — игнорирует ошибки кодирования. При этом игнорирование ошибок
# может привести к потере данных.
# ➢ 'replace' — вставляет маркер замены (например, '?') там, где есть
# некодируемые данные.
# ➢ 'namereplace' — при записи заменяет неподдерживаемые символы
# последовательностями \N{...}.
# ➢ errors='backslashreplace'

# newline - показывает как мы обрабатываем каждый конец строки внутри файла.
# closefd - указываем оставлять ли файловый дискриптор открытым по завершении работы с файлом и лучше его не трогать!
# opener - возможность самому прописать как открывать файл.

# кодировка нужно только в текстовом режиме - в бинарном не прописывается.

# errors='replace' - перемещать символы, которые содержат ошибку.

# Examples:
#
# import os
# import shutil
# from pathlib import Path
#
# for i in range(10):
#     with open(f'file_{i}.txt', 'w', encoding='utf-8') as f:  # от file_0.txt до file_9.txt
#         f.write('Hello world!')         # в каждый пишем фразу = Hello world!
# os.mkdir('new_dir')                     # создаем директорию new_dir
# for i in range(2, 10, 2):               # цикл перебирает файлы с четной цифрой и перемещает в new_dir
#     f = Path(f'file_{i}.txt')
#     f.replace('new_dir' / f)            # Из new_dir копирует всю инфу в dir_new
# shutil.copytree('new_dir', Path.cwd() / 'dir_new')
#
# #--------------------------------------------
#
# start = 10
# stop = 100
# with open('data.bin', 'bw+') as f:      # файл с бинарной двоичной информацией
#     for i in range(start, stop + 1):    # перебираем числа от 10 до 100 включительно. Кроме 100 все из 2-х цифр.
#         f.write(str(i).encode('utf-8')) # вместо 1 числа, записываем 2 цифры в кодировке utf-8
#         if i % 3 == 0:                  # числа кратные 3-м - затираются.
#             f.seek(-2, 1)               # делаем шаг от текущей позиции на -2
#     f.truncate(stop)                    # оставляем в файле только 100 символов
#     f.seek(0)                           # отправляем курсор в начало
#     res = f.read(start)                 # считываем от начала 10 байт
#     print(res.decode('utf-8'))          # выводим их на печать
#
# #----------------------------------------------
#
# # Для перехода на уровень выше можно использовать функцию os.path.dirname() из модуля os:
#
#
# # Получение текущей директории
# current_dir = os.getcwd()
#
# # Переход на уровень выше
# parent_dir = os.path.dirname(current_dir)
#
# # Выбор нужных файлов в родительской директории
# files = glob.glob(os.path.join(parent_dir, "*.txt"))
#
#
# # Также можно использовать метод
# os.path.join()
# # для создания пути к файлу или директории вне зависимости от операционной системы:
#
#
# # Создание пути к файлу в родительской директории
# file_path = os.path.join(parent_dir, "имя_файла.txt")
#
# # Проверка существования файла с определенным именем
# #     if os.path.isfile(f"{file_name}.{source_file_extension}")
#
# #----------------------------------------------
#
# # Для переименования файла в текущей директории можно использовать функцию os.rename() из модуля os:
#
#
# # Получение текущей директории
# current_dir = os.getcwd()
#
# # Переименование файла
# os.rename(os.path.join(current_dir, "старое_имя.txt"), os.path.join(current_dir, "новое_имя.txt"))
#
#
# # Также можно использовать метод rename() объекта Path из модуля pathlib:
#
# # Получение текущей директории
# current_dir = Path.cwd()
#
# # Переименование файла
# current_dir.joinpath("старое_имя.txt").rename(current_dir.joinpath("новое_имя.txt"))
#
# #------------------------------------------
#
# # Поменять директорию:
#
# # Для этого можно использовать метод chdir() из модуля os, который позволяет изменить текущую рабочую директорию.
# # Например, если нужно перейти в папку "Documents", можно написать следующий код:
#
# os.chdir("Documents") # переходим в папку "Documents"
#
# current_dir = os.getcwd()
# print(current_dir) # выведет путь к новой текущей директории "Documents"
#
#
# # Также можно использовать абсолютный путь к нужной директории вместо ее названия, чтобы быть уверенным,
# # что мы переходим именно в нужную директорию. Например:
#
# os.chdir("/Users/username/Documents") # переходим в папку "Documents" по абсолютному пути
#
# current_dir = os.getcwd()
# print(current_dir) # выведет путь к новой текущей директории "/Users/username/Documents"
#
#
# # Для получения пути к другой папке можно использовать функцию os.path.join(),
# # указав в нее путь к текущей директории и название нужной папки:
#
# current_dir = os.getcwd()
# target_dir = os.path.join(current_dir, 'название_папки')
# print(target_dir)
#
# # Также можно использовать функцию os.chdir() для изменения текущей рабочей директории на нужную:
#
# target_dir = '/путь/к/нужной/папке'
# os.chdir(target_dir)
# print(os.getcwd()) # путь к нужной папке
#
# #-----------------------------------------
#
# # Найти по имени файла путь
#
# def find_file_path(start_dir, file_name):
#     for root, dirs, files in os.walk(start_dir):
#         if file_name in files:
#             return os.path.join(root, file_name)
#     return None
#
# # Example usage
# start_dir = '/path/to/start/directory'
# file_name = 'example.txt'
#
# file_path = find_file_path(start_dir, file_name)
# if file_path:
#     print("File found at:", file_path)
# else:
#     print("File not found.")
#
# #----------------------------------------
# # найти папку по имени
#
# def find_nearest_folder(starting_directory, folder_name):
#     for root, dirs, files in os.walk(starting_directory):
#         if folder_name in dirs:
#             return os.path.join(root, folder_name)
#
#     return None
#
# starting_directory = "/path/to/starting_directory"
# folder_name = "folder_name"
#
# nearest_path = find_nearest_folder(starting_directory, folder_name)
# if nearest_path:
#     print("Nearest path to the folder:", nearest_path)
# else:
#     print("Folder not found.")
#
# ------------------------------
# Перемещаем файлы

import os
from pathlib import Path

# переименовали
# os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir',
# 'new_name.py'))
# оставили старое имя
# old_file = Path('new_name.py')
# new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)

# Создаю директорию
import os
from pathlib import Path

# print(os.getcwd())
# os.chdir('../..')
# print(Path.cwd())
# os.mkdir('files_execute')

# создаю директорию внутри директории

from pathlib import Path

# # Путь к родительской директории
# parent_dir = Path('//Users//РС//Documents//GEEKBRAINS//DATA_ENGINEER//Python//All_the_project//DE_py_HomeWorks',
#                   encoding='utf-8')
#
# # Имя новой директории
# new_dir = 'files_execute'
#
# # Полный путь к новой директории
# path = parent_dir / new_dir
#
# # Создание новой директории
# path.mkdir()


# удаляем по расширению файлов

# directory = '\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute'
# extension = '.txt'  # указанное расширение файлов
#
# file_list = glob.glob(os.path.join(directory, f'*{extension}'))
# for file_path in file_list:
#     os.remove(file_path)
#
# # -----------------------------------------
# # Родительская директория для файла представляет собой директорию, содержащую этот файл.
# file_path = DIRECTION
# parent_dir = os.path.dirname(file_path)
# print(f'Родительская директория для {file_path}: {parent_dir}')
# Родительская директория для \Users\РС\Documents\GEEKBRAINS\DATA_ENGINEER\Python\All_the_project: \Users\РС\Documents\GEEKBRAINS\DATA_ENGINEER\Python

# ------------------------------------------
# При использовании функции os.walk получаем кортежи с полными путями.
# Для каждого кортежа мы можем рассчитать относительный путь к родительской директории,
# используя функцию os.path.relpath.

# for dirpath, dirnames, filenames in os.walk('/путь/к/папке'):
#     for file in filenames:
#         full_path = os.path.join(dirpath, file)
#         rel_path = os.path.relpath(full_path, '/путь/к/папке')
#         print(f'Родительская директория для {file}: {rel_path}')
#
# # Для каждого файла можно получить родительскую директорию, используя функцию os.path.dirname.
# for dirpath, dirnames, filenames in os.walk('/путь/к/папке'):
#     for file in filenames:
#         full_path = os.path.join(dirpath, file)
#         parent_dir = os.path.dirname(full_path)
#         print(f'Родительская директория для {file}: {parent_dir}')

# DIRECTION = "\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project"
#
#
# def dir_to_json_csv_pickle(dir_path):
#     for dirpath, dirnames, filenames in os.walk(dir_path):
#         for file in filenames:
#             full_path = os.path.join(dirpath, file)
#             print(f'Родительская директория для {file}: {full_path}')
#
# # -----------------------------------
# # Получение информации о файле и размера по этой информации
#
# import os
#
# file_path = "example.txt"
#
# # получение информации о файле
# file_info = os.stat(file_path)
#
# # получение размера файла в байтах
# file_size = file_info.st_size
#
# print(f"Размер файла: {file_size} байт")
#
# # То же для каталога
#
# directory_path = "."
#
# # получение информации о каталоге
# directory_info = os.stat(directory_path)
#
# # получение размера каталога
# directory_size = directory_info.st_size
#
# print(f"Размер каталога: {directory_size} байт")
# # -------------------------

# создаем директорию

import os

os.chdir()
# создаем в пакете файл __init__.py
with open('__init__.py', 'w') as file:
    file.write('')