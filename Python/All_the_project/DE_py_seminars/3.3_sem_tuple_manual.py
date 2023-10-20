"""Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа."""

data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
# data = (('лиса', 45, 1, 'Mary', '6', 2.45, [1, 2, 3], (2, None), (2.3, 2.4), 8.16, 'music', [0, None]))
result = {}
for item in data:
    key = result.setdefault(type(item), list())
    key.append(item)

print(result)

#==================================================
"""
my_tuple = ('лиса', 45, 1, 'Mary', '6', 2.45, [1, 2, 3], (2, None), (2.3, 2.4), 8.16, 'music', [0, None])
int_list = []
str_list = []
tuple_list = []
float_list = []
else_list = []
list_list = []

for item in my_tuple:
    if type(item) == int:
        int_list.append(item)
    elif type(item) == float:
        float_list.append(item)
    elif type(item) == tuple:
        tuple_list.append(item)
    elif type(item) == str:
        str_list.append(item)
    elif type(item) == list:
        list_list.append(item)
    else:
        else_list. append(item)
new_dict = {'int': int_list, 'float': float_list, 'str': str_list,
            'list': list_list, 'tuple': tuple_list, 'else': else_list}

print(new_dict)
# print(int_list, str_list, list_list, tuple_list, float_list, else_list)
"""

