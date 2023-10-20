# locals()
# ----------------------------
# Возвращает словарь переменных из локальной области видимости НА МОМЕНТ ВЫЗОВА ФУНКЦИИ (ВСЕ, ЧТО ДО)

SIZE = 10


def func(a, b, c):
    x = a + b
    print(locals()) #  {'a': 1, 'b': 2, 'c': 3, 'x': 3} !!! Эти данные на чтение, не изменить!!!

    z = x + c
    return z


func(1, 2, 3)

# globals()
# ----------------------------
# Возвращает словарь переменных из глобальной области видимости на момент вызова функции

SIZE = 10


def func(a, b, c):
    x = a + b
    print(globals())        # !!! Можем изменить переменную globals по ключу.

    z = x + c
    return z

print(globals())
print(f'{func(1, 2, 3) = }')

# изменяем словарь globals
x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(f'{x = }')

# vars()
# ----------------------------
# Без аргументов то же, что и locals. Если передать объект, вернет его аттрибут __dict__.
# Если такого аттрибута нет - вызовет ошибку.

# Смотрим какие внутренние методы есть у функции int
print(vars(int))