"""3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions"""
"""
import fractions


def multiplation(n1: int, n2: int, d1: int, d2: int):
    dividend = n1 * n2
    divisor = d1 * d2
    i = 2
    div = dividend if dividend > divisor else divisor
    while i < div ** 0.5 + 1:
        while dividend % i == 0 and divisor % i == 0:
            dividend //= i
            divisor //= i
        i += 1
    if dividend == divisor:
        return 1
    elif dividend % divisor == 0:
        return dividend // divisor
    else:
        return f'{dividend}/{divisor}'


def summation(n1: int, n2: int, d1: int, d2: int):
    if d1 != d2:
        n1 = n1 * d2
        n2 = n2 * d1
        d1 = d2 = d1 * d2
    if d1 == d2:
        dividend = n1 + n2
        divisor = d1
        div = dividend if dividend > divisor else divisor
        i = 2
        while i < div ** 0.5 + 1:
            while dividend % i == 0 and divisor % i == 0:
                dividend //= i
                divisor //= i
            i += 1
        if dividend == divisor:
            return 1
        elif dividend % divisor == 0:
            return dividend // divisor
        else:
            return f'{dividend}/{divisor}'

    numerator = n1 + n2
    denominator = d1
    if numerator > denominator:
        priv_remain = divmod(numerator, denominator)
        return f'{priv_remain[0]}{priv_remain[1]}/{denominator}'
    elif numerator == denominator:
        return numerator // denominator
    else:
        return f'{numerator}/{denominator}'


MULTIPLICATION = 'п'
SUM = 'с'
EXIT = 'в'
START = 'н'
while True:
    f = True
    while f:
        n_1 = input(f'Введите первую дробь вида "a/b" или '
                    f'введите {EXIT}, чтобы выйти.\n')
        if n_1 == 'в':
            quit('Пока!')
        char = '/'
        count = n_1.count(char)
        if count == 1:
            num1, num2 = n_1.split('/')
            if num1.isdigit() and num2.isdigit():
                print(f'Вы ввели: {n_1}')
                n_1 = fractions.Fraction(int(num1), int(num2))
                f = False
            else:
                print('Вы ввели неправильное значение. Попробуйте снова')
        else:
            print('Вы ввели неправильное значение. Попробуйте снова')

    f = True
    while f:
        n_2 = input(f'Введите вторую дробь вида "a/b" или '
                    f'введите {EXIT}, чтобы выйти.\n')
        if n_1 == 'в':
            quit('Пока!')
        char = '/'
        count = n_2.count(char)
        if count == 1:
            number1, number2 = n_2.split('/')
            if num1.isdigit() and number2.isdigit():
                print(f'Вы ввели: {n_2}')
                n_2 = fractions.Fraction(int(number1), int(number2))
                f = False
            else:
                print('Вы ввели неправильное значение. Попробуйте снова')
        else:
            print('Вы ввели неправильное значение. Попробуйте снова')

    while True:
        action = input(f'Выберите дальнейшее действие: \n'
                       f'Произведение: {MULTIPLICATION} '
                       f'Cумма: {SUM} '
                       f'Выйти: {EXIT} '
                       f'Вернуться к вводу чисел: {START}\n')
        if action == 'в':
            quit('Пока!')
        elif action == 'п':
            print(multiplation(int(num1), int(number1), int(num2), int(number2)))
            print(f'{n_1} * {n_2} = {n_1 * n_2}')
            continue
        elif action == 'с':
            print(summation(int(num1), int(number1), int(num2), int(number2)))
            print(f'{n_1} + {n_2} = {n_1 + n_2}')
            continue
        elif action == 'н':
            break
"""
#=================================================================

from fractions import Fraction

a1, b1 = [int(i) for i in input("Введите первую дробь через/").split("/")]
a2, b2 = [int(i) for i in input("Введите вторую дробь через/").split("/")]
s = (a1 * b2 + a2 * b1) / (b1 * b2)
p = (a1 * a2) / (b1 * b2)
a = Fraction(a1, b1)
b = Fraction(a2, b2)
print(f"{s} = {a + b}, {p} = {a * b}")

