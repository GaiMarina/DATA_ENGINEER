"""Программа загадывает число от 0 до 1000.
Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 1
num = randint(LOWER_LIMIT, UPPER_LIMIT)
while count <= 10:
    while True:
        n = int(input(f'Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT} за 10 попыток. Попытка № {count}: '))
        if n < 0 or n > 1_000:
            print('Я вас не понимаю. Попробуйте снова: ')
        else:
            break
    print('Вы ввели число ' + str(n))
    count += 1
    if n == num:
        print('Вы молодец! Угадали!')
        break
    else:
        print('Больше') if n < num else print('Меньше')

print(f'Исчерпаны все попытки. Сожалею.')
print('Я загадал ' + str(num))
