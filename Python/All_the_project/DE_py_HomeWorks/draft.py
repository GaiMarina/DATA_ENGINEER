from pathlib import Path
import os

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

# os.chdir('//Users//РС//Documents//GEEKBRAINS//DATA_ENGINEER//Python//All_the_project//DE_py_HomeWorks//files_execute')
# print(Path.cwd())

# копирование файлов
import shutil

# shutil.copy('\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_seminars\\7.1_sem_1000_1000.py', 'files_execute')
#
# shutil.copy('\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_seminars\\7.2_sem_pseudonyms.py', 'files_execute')
# shutil.copy('\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_seminars\\7.3_usint_7.2_7.1.py', 'files_execute')
# shutil.copy('\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_seminars\\7.4_file_generator.py', 'files_execute')
# shutil.copy('\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_seminars\\7.5_sem_sort_file_to_dir.py', 'files_execute')


# os.rename('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute\\7.1_sem_1000_1000.py', 'int_float_pairs.py')
# os.rename('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute\\7.2_sem_pseudonyms.py', 'pseudonyms_generator.py')
# os.rename('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute\\7.3_usint_7.2_7.1.py', 'nums_names_processing.py')
# os.rename('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute\\7.4_file_generator.py', 'random_files_generator.py')
# os.rename('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute\\7.5_sem_sort_file_to_dir.py', 'sort_files_to_dirs.py')

# os.chdir('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute')
# # Path('7.1_sem_1000_1000.py').rename('int_float_pairs.py')
# Path('7.2_sem_pseudonyms.py').rename('pseudonyms_generator.py')
# Path('7.3_usint_7.2_7.1.py').rename('nums_names_processing.py')
# Path('7.4_file_generator.py').rename('random_files_generator.py')
# Path('7.5_sem_sort_file_to_dir.py').rename('sort_files_to_dirs.py')

# удаляем по расширению файлов
# import glob
# from random import random
#
# directory = '\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute'
# extension = '.txt'  # указанное расширение файлов
#
# file_list = glob.glob(os.path.join(director f'*{extension}'))
# for file_path in file_list:
#     os.remove(file_path)y,

# размер
# print(os.path.getsize('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute\\Jhpttcbgbungcylcldrjrh.txt'))

# # генерируем случайное число байт от 1 до 100
# num_bytes = random.randint(1, 100)
#
# # открываем файл для записи в бинарном режиме
# with open("random_bytes.bin", "wb") as f:
#     # генерируем случайные байты и записываем их в файл
#     for i in range(num_bytes):
#         # генерируем случайный байт от 0 до 255
#         byte = random.randint(0, 255)
#         # преобразуем число в байтовую строку и записываем в файл
#         f.write(byte.to_bytes(1, "big"))

# shutil.copy('\\Users\\РС\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\7_hw_group_file_rename.py', 'files_execute')

os.chdir('\\Users\\РС\\Documents\\GEEKBRAINS\\DATA_ENGINEER\\Python\\All_the_project\\DE_py_HomeWorks\\files_execute')
Path('hw_group_file_rename.py').rename('HW_group_file_rename.py')
