"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним."""

a = float(input('Введите а: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

if (a + b) > c and (b + c) > a and (a + c) > b:
    print('Это треугольник')
    if a == b and b == c and a == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or a == c:
        print('Треугольник равнобедренный')
    elif a != b and b != c and a != c:
        print('Треугольник разносторонний')
else:
    print('Это не треугольник')
