""" Запросить у пользователя число и нарисовать елочку.
Число 5 => 5 рядов.

    *
   ***
  *****
 *******
*********
"""
"""
a = int(input('Введите число: '))
count = 1
STEP = 2
count_2 = 1
for i in range(1, a + 1):
    print(f' ' * (a - count), '*' * count_2, f' ' * (a - count))
    count += 1
    count_2 += STEP
"""
#---------------------------------------

SPACE = ' '
STAR = '*'

rows = int(input('Сколько рядов у елки? '))
spaces = rows - 1
stars = 1

for i in range(rows):
    print((SPACE * spaces) + (STAR * stars))
    stars += 2
    spaces -= 1