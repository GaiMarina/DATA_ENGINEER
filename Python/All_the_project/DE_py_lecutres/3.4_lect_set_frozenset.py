# Множества - НЕИЗМЕНЯЕМЫЙ ТИП (можно обернуть список в кортеж и тогда можно включить в множество)
"""
# Изменяемое множество:
my_set = {1, 2, 3, 4, 5, 6, 7}

# Не изменяемое множество:
my_f_set = frozenset((1, 2, 3, 4, 5, 6, 7,))

# метод .add()

my_set.add(9)
print(my_set)

# Два значения в скобках добавить нельзя, можно добавить кортеж:
my_set.add((8, 9))
print(my_set)


# .remove() Удаляет элемент по значению
my_set = {1, 2, 3, 4, 5, 6, 7}
my_set.remove(6)
print(my_set)

# Метод .discard()

my_set = {1, 2, 3, 4, 5, 6, 7}
my_set.discard(7)
print(my_set)
my_set.discard(10)      # не найдет такое значение, но НЕ выведет ошибку как remove()


# .intersection() Выводит множество элементов, которые есть и в том и в другом множестве.

my_set = {1, 2, 3, 4, 5, 6, 7}
other_set = {10, 20, 3, 4, 5, 60}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\t {other_set = }\t {new_set =}')

# То же самое через &
my_set = {1, 2, 3, 4, 5, 6, 7}
other_set = {10, 20, 3, 4, 5, 60}
new_set = my_set & other_set
print(f'{my_set = }\t {other_set = }\t {new_set =}')


# .union() Объединяет элементы из первого и из второго множества

my_set = {1, 2, 3, 4, 5, 6, 7}
other_set = {10, 20, 3, 4, 5, 60}
new_set = my_set.union(other_set)
print(f'{my_set = }\t {other_set = }\t {new_set =}')

# То же через |
new_set = my_set | other_set
print(f'{my_set = }\t {other_set = }\t {new_set =}')
"""

# Метод .difference() - разность множеств. Выводятся элементы первого мн-ва, которые не повторяются во втором.
# Элементы второго мн-ва не учитываются.

my_set = {1, 2, 3, 4, 5, 6, 7}
other_set = {10, 20, 3, 4, 5, 60}
new_set = my_set.difference(other_set)
print(f'{my_set = }\t {other_set = }\t {new_set =}')

# То же через -
new_set = my_set - other_set
print(f'{my_set = }\t {other_set = }\t {new_set =}')



