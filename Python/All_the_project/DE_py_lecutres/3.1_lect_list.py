# Список
"""list1 = list()
list2 = []

# extend

a = 'Hello World!'
b = [None]
b.extend(a)
print(b)            # [None, 'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!'] (.append() добавляет элемент целиком)

# !!! Через append() нельзя ссылаться на себя: а.append(a), а через extend() - можно, например, удвоить список.
b.extend(b)
print(b)


# .pop() удаляет и одновременно сохраняет в переменную либо по индексу в круглых скобках, либо 1 элемент с конца.

my_list = [1, 2, 3, 4]
b = my_list.pop()
print(my_list, b)
b = my_list.pop(1)
print(my_list, b)

# count() - количество вхождений в список

my_list = [1, 2, 3, 2, 4, 2, 5]
b = my_list.count(2)
print(b)  # 3 двоечки в списке

# метод index() - индекс первого вхождения элемента в список. Ищем по значению! Можно задать диапазон для поиска

my_list = [1, 3, 2, 4, 3, 5, 6]
b = my_list.index(3)
print(b)  # 1
c = my_list.index(3, b + 1, 90)
# ищем опять 3, начиная со следующего элемента. Выход за пределы списка не даст ошибку. Если элемента нет - выдаст ошибку.


# insert(1, 2) 1 - индекс куда добавлять, 2 - само число, которое вставляем. Исходный список увеличивается на 1 элемент.
# Отрицательный индекс insert(-2, 2) вставит двойку 3-ей с конца

# Метод .pop() удаляет по индексу. А метод - .remove() - по значению.

# sorted()

my_list = [1, 3, 4, 2, 6, 7, 8]
sorted_list = sorted(my_list)
print(my_list)
print(sorted_list, sep='\n')                # Создаем новый отсортированный объект
sorted_list = sorted(my_list, reverse=True)
print(sorted_list, sep='\n')

# .sort(), если нужно отсортировать существующий список. Работает только со списками.
my_list.sort(reverse=True)
print(my_list)

tuple_list = ((8, 9), (1, 2), (2, 3), )
sorted_tuple = sorted(tuple_list, reverse=True)
print(sorted_tuple)


# функция reversed()
my_list = [2, 6, 54, 3, 7]
res = reversed(my_list)
print(type(res), res) # объект, если хотим получить список - обернуть в list

rev_list = list(reversed(my_list))
print(rev_list)

# Когда нужно перебрать элементы справа налево:

for i in reversed(my_list):
    print(i)

# Метод reverse() разворачивает элементы списка не создавая новый объект.
my_list = [2, 6, 54, 3, 7]
my_list.reverse()                   # Развернули
my_list2 = my_list[::-1]            # Вернули как был.
print(my_list, my_list2, sep='\n')


# Создание копии.
# Ссылка у обоих списков на одну ячейку => оба списка изменились.
my_list = [2, 6, 54, 3, 7]
new_list = my_list
print(new_list, my_list, sep='\n')
my_list[2] = 555
print(new_list, my_list, sep='\n')

# .copy() создает поверхностную копию списка.

my_list = [2, 6, 54, 3, 7]
new_list = my_list.copy()
print(new_list, my_list, sep='\n')
my_list[2] = 555
print(new_list, my_list, sep='\n')


# Матрицы и .copy()
# Изменятся оба списка т.к. копия поверхностная и затрагивает только первый уровень вложенности.
matrix = [[1, 3, 2], [9, 0, 9], [34, 5, 4]]
new_matrix = matrix.copy()
print(matrix, new_matrix, sep='\n')
matrix[0][1] = 555
print(matrix, new_matrix, sep='\n')

from copy import deepcopy
# deepcopy рекурсивно обходит все структуры любой глубины вложенности
matrix = [[1, 3, 2], [9, 0, 9], [34, 5, 4]]
new_matrix = deepcopy(matrix)
print(matrix, new_matrix, sep='\n')
matrix[0][1] = 555
print(matrix, new_matrix, sep='\n')
"""

# len()

my_list = [2, 6, 54, 3, 7]
matrix = [[1, 3, 2, 4, 5], [9, 0, 9, None], [34, 5, 4]]
print(len(my_list))     # 5
print(len(matrix))      # 3
print(len(matrix[1]))   # 4
