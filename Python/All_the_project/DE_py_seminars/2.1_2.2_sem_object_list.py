"""Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные. """

"""
a = 45
b = 2.3
c = ()
print(type(a), type(b), type(c))
"""
# =========================================
"""
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. 

Для каждого элемента в цикле выведите:

- порядковый номер начиная с единицы
- значение
- адрес в памяти
- размер в памяти
- хэш объекта
- результат проверки на целое число только, если он положительный
- результат проверки на строку только если он положительный

Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

import sys
data = [42, 73.0, 'Hello world!', True, 42, 42, 'Hello world!', 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']
for i, item in enumerate(data, start=1):
    check_int = 'Похоже на целое число' if isinstance(item, int) else ''
    check_str = 'Это строка' if isinstance(item, str) else ''
    print(f'{i}. Объект {item}\nАдрес: {id(item)}\tРазмер: {sys.getsizeof(item)} байт'
          f'\tХэш: {hash(item)} {check_int}{check_str}', end='\n')


#===============================

# порядковый номер с 1
"""
data = [5, 'abs', 2.3, (1, 2), [3, 4, 5]]
for i, j in enumerate(data, start=1):
    print(i)

# значение

for i, j in enumerate(data):
    print(j)
"""
# адрес в памяти
"""
data = [5, 'abs', 2.3, (1, 2), [3, 4, 5]]
for i, j in enumerate(data):
    print(j, ' - ', id(j))
 #======================================
 #.__sizeof__() Сколько байт занимает в памяти

for i, j in enumerate(data):
    print(j, ' - ', j.__sizeof__(), ' байт.')

#=====================================

# хэш объекта
print()
for i, j in enumerate(data):
    print(j, ' - ', hash(j))
"""
#========================================
"""
data = [5, 'abs', 2.3, (1, 2), [3, 4, 5], True]
for i, j in enumerate(data):
    check_int = f'{j} - похоже на целое число' if isinstance(j, int) else f'{j} - '
    check_str = f'{j} - это строка' if isinstance(j, str) else f'{j} - '
    print(check_int, check_str)
"""