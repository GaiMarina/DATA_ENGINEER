""" Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n. """

e = int(input('Введите е: '))
n = int(input('Введите  n: '))
STEP = 2
sum_total = 0
count = STEP
while count < n:
    if count % e == 0:
        count += STEP
        continue
    sum_total += count
    count += STEP
print(sum_total)
