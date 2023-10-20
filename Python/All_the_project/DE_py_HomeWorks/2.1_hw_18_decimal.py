"""2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""

num = int(input('Введите число: '))
num2 = num
s = '0123456789ABCDEF'
base = 16
res = ''

while num > 0:
    res = s[num % base] + res
    num = num // base

print(res)
print('Проверка: ', hex(num2)[2:])

# =========================================
"""
HEX = 16
num: int = int(input('Введите число: '))
n = num
s = '0123456789abcde'
res = ''
while num > 0:
    num, remainder = divmod(num, HEX)
    res = s[remainder] + res

print(f'Шестнадцатеричное строковое представление числа {n} - {res}.\n'
      f'Через функцию HEX - {hex(n)}')

# Ox - вначале означает шестнадцатеричную систему.
"""