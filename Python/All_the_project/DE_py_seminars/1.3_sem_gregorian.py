"""
year = int(input('Введите год в формате yyyy: '))
if year < 1582:
    print('Ошибка!')
elif year % 4 != 0:               # Високосный: год, номер которого кратен 4, НО ИЛИ кратен 400 или НЕ кратен 100
    print("Обычный")            # 1582 - ввод Грегорианского календаря
elif year % 100 == 0:
     if year % 400 == 0:
        print("Високосный")
     else:
        print("Обычный")
else:
    print("Високосный")
"""

year = int(input('Введите год в формате yyyy: '))
if year < 1582:
    print('Ошибка!')
elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('Високосный год')
else:
    print('Невисокосный год')