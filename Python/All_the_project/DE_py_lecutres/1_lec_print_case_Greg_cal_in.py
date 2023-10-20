# print('Hello', ',', 'world', '!', sep='/', end='\n(=^.^=)\n')

# ---------------------------------

# match - case
"""
color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зелёный':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')
"""
# ---------------------------------

# Високосный год
"""
year = int(input('Введите год в формате yyyy: '))
if year % 4 != 0:               # 1. год, номер которого кратен 4, — високосный
    print("Обычный")            # 2. год, номер которого кратен 400, — високосный;
elif year % 100 == 0:           # 3. год, номер которого кратен 100, — невисокосные
     if year % 400 == 0:        # 4. все остальные годы — невисокосные.
        print("Високосный")
     else:
        print("Обычный")
else:
    print("Високосный")
"""
# -------------------------------------
"""
year = int(input('Введите год в формате yyyy: '))
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print("Обычный")
else:
    print("Високосный")
"""
# ----------------------------
"""
data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num in data:
    print('Леонардо передаёт привет!')

# А теперь тот же самый код, но с конструкцией not — отрицание:

data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
num = int(input('Введи число: '))
if num not in data:
    print('Леонардо грустит :-(')
"""
#-------------------------------------
"""
animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
for i, animal in enumerate(animals, start=1):
    print(i, animal)
"""
#-----------------------------------
"""
data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
            break
else:
    data += 5
print(data)
"""

#------------------------------

# while True

min_limit = 0
max_limit = 10
while True:
    print('Введи число между', min_limit, 'и', max_limit, '? ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
    print('Было введено число ' + str(num))

#------------------------------

min_limit = 0
max_limit = 10
count = 3
while count > 0:
    print('Попытка ' + str(count))
    count -= 1
    num = float(input('Введи число между ' + str(min_limit) + ' и\
    ' + str(max_limit) + ': '))
    if num < min_limit or num > max_limit:
        print('Неверно')
    else:
        break
else:
    print('Исчерпаны все попытки. Сожалею.')
    quit()
print('Было введено число ' + str(num))