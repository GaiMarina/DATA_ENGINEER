# max() / min()
# -------------
# Принимает итератор или аргументы. Можно передать key или default
"""
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [('Иван', 25_000), ('Александр', 30_000), ('Максим', 90_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))
"""
# sum()
# -------------
# Принимает итератор или аргументы. Можно передать start

my_list = [42, 234, 56]
print(sum(my_list))
print(sum(my_list, start=1024)) # общая сумма суммируется со значением start
