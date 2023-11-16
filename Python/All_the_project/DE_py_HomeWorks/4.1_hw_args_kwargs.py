"""Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
(кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""


def func() -> None:     # В locals() переменную нельзя изменить, а в globals() - можно!!! (Обе ф-и возвр-т словарь)
    g = globals()
    change = {}
    for key, value in g.items():
        if key == 's':
            continue
        if key.endswith('s'):
            change[key[:-1]] = g[key]
            g[key] = None
    for key, value in change.items():
        g[key] = value


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

print(func())
print(globals())

#============================================================
"""
def s_object_replace(**kwargs):
    print(kwargs)
    kwargs_dict = {}
    for obj, m in kwargs.items():
        if obj.endswith('s') and len(obj) > 1:
            kwargs_dict[obj] = None
            obj_2 = obj[:-1]
            kwargs_dict[obj_2] = m
        else:
            kwargs_dict[obj] = m
    return kwargs_dict


print(s_object_replace(wars='wars', calls='calls', nos='nos', s='s', abscence='abscence'))
"""