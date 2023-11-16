"""Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def path_name_extension(p: str) -> tuple:
    *_, n_ext = p.split('/')
    *n, ext = n_ext.split('.')
    if len(n) > 1:
        n = '.'.join(n)
    return p, n, ext


path = "/Users/РС/Documents/GEEKBRAINS/DATA_ENGINEER/Python/Py_HWs/4.4_py_hw.py"
print(path_name_extension(path))

