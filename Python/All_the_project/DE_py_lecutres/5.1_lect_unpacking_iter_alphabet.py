a, b, c = ['a', 'b', 'c', ]
print(f'{a=}, {b=}, {c=}')

data = ['один', 'два', 'три', 'четыре', 'пять']
a, b, *c = data  # !!! Звездочкой можно пометить только одну переменную!
print(f'{a=}, {b=}, {c=}')

print('***' * 20)

link = 'https://fun.lordseriala.fun/493-velikaja.html'
prefix, *_, suffix = link.split('/')
print(f'{prefix=}{suffix=}')

print('***' * 20)

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')  # аналог for i in data print()...

print('***' * 20)

a, b, c, d = [2, 4, 6, 8]
a, b, c, d = d, c, b, a
print(a, b, c, d)  # 8 6 4 2

print('***' * 20)
print('***' * 20)

# iter(object[, sentinel])

# a = 42
# iter(a) # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(
    *list_iter)  # объект итератор создается только 1 раз. После print(*list_iter) надо создать заново для 2-го принта.
print(list_iter)

print('***' * 20)

import functools

f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):  # b'' - пустая бинарная строка, 2-й аргумент iter()
    print(block)                            # на 16 блоков
f.close()

print('***' * 20)
print('***' * 20)

# next(iterator[, default])

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter, 42))
print(next(list_iter, 42))  # Дефолтное значение
print(next(list_iter, 42))

print('***' * 20)
print('***' * 20)

# Генераторы
# Вывод по букве алфавита

my_gen = (chr(i) for i in range(97, 123))
print(my_gen)
for char in my_gen:
    print(char)

print('***' * 20)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')

print('***' * 20)

# List comprehensions

my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp)
for char in my_listcomp:
    print(char)

print('***' * 20)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)  # Генератор не хранит сразу весь список как []
# () => м.использовать генераторное выражение для функции iter(), перебора через цикл for или для next()
for item in mult:
    print(f'{item = }')

print('***' * 20)

# set, dict comprehensions

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res) = }\n{res}')

print('***' * 20)

my_dict_comp = {i: chr(i) for i in range(97, 123)}
print(my_dict_comp)
for number, char in my_dict_comp.items():
    print(f'dict[{number}] = {char}')

print('***' * 20)
print('***' * 20)


def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result


for i, num in enumerate(factorial(10), start=1):
    print(f'{i}!={num}')

print('***' * 20)


# yield
def factorial_gen(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number


for i, num in enumerate(factorial_gen(10), start=1):
    print(f'{i}!={num}')

print('***' * 20)

# iter() + next()

my_iter = iter(factorial_gen(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))