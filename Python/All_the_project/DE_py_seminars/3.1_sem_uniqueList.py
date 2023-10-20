"""Вручную создайте список с целыми числами, которые повторяются. Получите новый список,
который содержит уникальные (без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков."""

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

list_from_set = list(set(data))
print(f'{data = }\n{list_from_set = }')

new_list = []
for item in data:
    if item not in new_list:
        new_list.append(item)
print(f'{data = }\n{new_list = }')

#==================================================
"""
my_list = [1, 2, 5, 2, 4, 3, 4, 2, 3, 2, 4]
print(my_list)

# Через set

new_list = set(my_list)
print(list(new_list))

new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

"""