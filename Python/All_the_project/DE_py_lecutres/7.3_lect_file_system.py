# Работа с каталогами

# Получение текущего пути:

import os
from pathlib import Path        # более современный модуль

print(os.getcwd())  # current work dir
print(Path.cwd())   # с большой буквы => это класс

os.chdir('../..')       # Перейти на 2 папки выше

print(os.getcwd())
print(Path.cwd())

# Создать директорию (т.е.папку, каталог)

os.mkdir('new_os_dir')
Path('new_path_dir').mkdir()

# Создание директорий с несколькими уровнями вложенности

os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir').mkdir(parents=True) # Указываем создание родительских директорий.

# Удаляем директории

os.rmdir('name')
Path('some_dir/dir/new_path_dir').rmdir()
# удаляет только пустые директории, т.е. если есть вложенные папки - прописывать весь путь для удаления

# Перемещаем файлы из каталога в каталог:

import shutil

shutil.rmtree('dir/other_dir')      # Удалили в dir внутренний каталог и файл, который был в нем
shutil.rmtree('some_dir')

# Функция join() - для правильного формирования пути.

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_2 = }\n{file_2}')

# Чтение данных о каталогах

print(os.listdir())     # выводит имена каталогов, файлов (все, что в текущей рабочей области)

p = Path(Path().cwd())  # p хранит инфу из текущей раб.области, с которой можно работать.
for obj in p.iterdir(): # .iterdir() обходит все, что в рабочей области как итератор
    print(obj)


# Проверяем что конкретно перед нами:

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')     # является ли директорией
    print(f'{os.path.isfile(obj) = }', end='\t')    # является ли файлом
    print(f'{os.path.islink(obj) = }', end='\t')    # является ли ссылкой
    print(f'{obj = }')

p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')

# Проходимся по всей иерархии

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }')
# dir_name = даст названия директорий и ходить будем по ним по всем.

# Переименовать файл:

os.rename('old_name.py', 'new_name.py')

p = Path('old_file.py') # передали файл в p
p.rename('new_file.py')
# более короткая запись
Path('new_file.py').rename('newest_file.py')

# перенести файл в др.место

# здесь в процессе переноса еще и меняется имя файла!
os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))

old_file = Path('new_name.py')
# здесь перенос без изменения имени: old_file, с сохранением old_file
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)

# копируем файлы

shutil.copy('one.txt', 'dir')
# здесь файл не только скопирован, но и переименован. Сохраняются и метаданные, если есть.
shutil.copy2('two.txt', 'dir/one_more.txt')
# копируем целые директории
shutil.copytree('dir', 'one_more_dir') # создаст еще одну папку с другим именем, но тем же содержимым.

# удалить директорию

shutil.rmtree(('dir'))

os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()