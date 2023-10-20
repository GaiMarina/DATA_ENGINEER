"""Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
(кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
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
