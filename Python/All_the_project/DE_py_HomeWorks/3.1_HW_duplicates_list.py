"""Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов."""

my_list = [2, 2, 4, 3, 7, 5, 2, 4, 3, 8, 8, 9, 67, 23, 45, 67, 34]
result_list = []

for num in set(my_list):
    if my_list.count(num) > 1:
        result_list.append(num)
    else:
        continue

print(result_list)
