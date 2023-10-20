# То же, что и список, только не изменяемый!!!
# функция len(), методы count(), index()

# Чтобы функция опознала объект как кортеж, скобок д.б.по 2: f((2, 3))

# ==========================================
"""
# Dictionaries

a = {'one': 42, 'two': 3.14, 'ten': 'Hello World!'}
b = dict(one=42, two=3.14, ten='Hello World!')
# Список с тремя элементами кортежа
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello World!')])
print(a == b == c)

# dict[key] - значения после равно - поиск по ключу.
# dict.get(key[, default]) - доступ к значению через метод get()


TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two'])
print(my_dict[TEN])
# print(my_dict[1]) # ошибка - несуществующий ключ

# Метод get()
# Если не нашел ключ, выводит - None. Если добавить 2-й аргумент, не найдя ключ выведет значение по дефолту.
print(my_dict.get('five', 5))



# setdefault()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(my_dict)  # Добавил 'five': None
print(f'{spam = }\t{my_dict = }')

eggs = my_dict.setdefault('six', 6) # Добавит ключ: значение, которых не было
print(f'{eggs = }\t{my_dict = }')

new_spam = my_dict.setdefault('two')
print(f'{spam = }\t{my_dict = }')   # Словарь не изменится, т.к. такой ключ уже есть, в переменную попадет значение ключа.

new_egg = my_dict.setdefault('one': 1_000)
print(f'{spam = }\t{my_dict = }')   # 1_000, кот.по умолчанию не пригодилась, т.к. ключ такой есть и выводится его значение.


# .keys()
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for item in my_dict.keys():
    print(item, end=' ')

# !!! По умолчанию даже без .keys() будет итерация по ключам, как в примере выше.

# .values()

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for item in my_dict.values():
    print(item, end=' ')


# .items()

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())  # dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('ten', 10)])

for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')


# .popitem() Удаляет последнюю пару ключ: значение

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')


# .pop() Удаляет значение по ключу.
# В отличие от списков, если не передать в .pop() значение реально существующего ключа, будет ошибка.

# Метод .update()

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6)) # передаем новый словарь
print(my_dict)

my_dict.update(dict([('two', 42), ('six', 6)]))
print(my_dict) # Ключ two уже был => он обновляется, но остается на своей старой позиции, там, где и был.
"""
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict = my_dict | {'six': 6, 'eigth': 8} | dict(six=6)
print(my_dict)

# В записи словаря запятая даже после последнего элемента!!!

# Словари сохраняют порядок, в котором были добавлены записи. Если удалить ключ: значение и по этому же ключу заново добавить
# заново ключ:значение добавится уже в конец.