"""Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
"""

new_str = input('Введите 2 числа через пробел: ')


def unicode_dict(nums: str) -> dict:
    nums = [int(n) for n in new_str.split()]
    dict_unicode = dict(sorted({chr(num): num for num in nums}.items(), key=lambda x: x[1]))
    return dict_unicode


print(unicode_dict(new_str))
