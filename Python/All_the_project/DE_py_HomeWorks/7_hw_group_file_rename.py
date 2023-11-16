"""Напишите функцию группового переименования файлов.
Она должна:
- принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""
import os
from pathlib import Path


def files_renaming(digits_num: int,
                   fname_char_range: list[int],
                   source_file_extension: str,
                   final_file_extension: str,
                   desired_name=''
                   ):
    """Group given extension files renaming function"""
    current_dir = os.getcwd()  # нашли текущую папку
    print(current_dir)
    n = 10 ** (digits_num - 1)
    # fin_n = 10 ** digits_num
    a, b = fname_char_range
    for dir_path, dirs_names, files_names in os.walk(current_dir):
        for file_name in files_names:
            if os.path.splitext(file_name)[1] == source_file_extension:
                original_name_range = os.path.splitext(file_name)[0].split('\\')[-1]  # название
                original_name_range = original_name_range[a:b]  # кусок бывшего названия
                new_file_name = ''.join(original_name_range) + desired_name + f'{n}' + final_file_extension
                print(new_file_name)
                Path(file_name).rename(new_file_name)
                n += 1
                continue


desired_file_name = 'new'

file_extention = '.txt'  # source_file_extension splitext - кортеж: путь + расширение

desired_file_extension = file_extention

original_file_name_range = [3, 6]
digits_num = 3

while True:
    try:
        source_folder_path = 'DE_py_seminars'
        current_direction = os.getcwd()  # получили текущую директорию
        target_dir = os.path.join(current_direction, source_folder_path)  # получили нужную директорию
        os.chdir(target_dir)
    except:
        os.chdir('./..')
    finally:
        source_folder_path = 'DE_py_seminars'
        current_direction = os.getcwd()  # получили текущую директорию
        target_dir = os.path.join(current_direction, source_folder_path)  # получили нужную директорию
        os.chdir(target_dir)
        break

files_renaming(digits_num,
               original_file_name_range,
               file_extention,
               desired_file_extension,
               desired_file_name)
