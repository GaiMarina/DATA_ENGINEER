# # только позиционная функция
#
# def pos_only_arg(arg, /):
#     print(arg)  # функции лучше без принтов
#
# pos_only_arg(42)
# # pos_only_arg(arg=42)  выдаст ошибку
#
# #===================================================
#
# # Только ключевая функция
#
# def kwd_only_arg(* ,arg):
#     print(arg)  # функции лучше без принтов
#
# kwd_only_arg(arg=42)
# # pos_only_arg(42)  выдаст ошибку
#
#
# #=================================================
# Все варианты параметров

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# combined_example(1, 2, 3) # takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # got some positional-only arguments passed as keyword arguments: 'pos_only'



# # -----------------------
# # *args (любое кол-во позиционных аргументов), **kwargs(любое кол-во ключевых)
# # М.б.и те и те: позиционные попадают в *args как в кортеж, ключевые в **kwargs - как в словарь
# # -----------------------
#
# def mean(args):
#     return sum(args) / len(args)
#
# # print(mean(1, 2, 3)) takes 1 positional argument but 3 were given
# print(mean([1, 2, 3]))
#
#
# def mean(*args):
#     return sum(args) / len(args)
#
#
# print(mean(1, 2, 3))
# print(mean(*[1, 2, 3]))
#
#
# def school_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f'По предмету {key} получена оценка {value}')
#
# school_print(химия=5, математика=3, русский=2, физра=4)
#
#
# # ------------------------------------------
# # Локальная область видимости: x, nonlocal(x), global(x)
# # ------------------------------------------
# #----------------------
# # lambda
# #-------------------------