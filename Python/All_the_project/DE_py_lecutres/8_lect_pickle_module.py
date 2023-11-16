# занимается сериализацией. Преобразует в байты и назад.

# можно работать только с данными, в безопасности которых уверены. Сам pickle не проверяет на безопасность!

# import pickle
# import os
#
# res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")  # преобразуем в данные набор байт через pickle
# print(f'{res = }')
#
# os.system('echo Hello World!')  # echo выводит на экран сообщение

# ---------------------------
# Сериализация
# ----------------------------

import pickle

# pickle.dump(my_dict, f)
# сохранение объекта в бинарном файле
#
# result = pickle.dumps(my_dict)
# сохранение объекта в строку байт.

# my_dict = {
#     "first_name": "Джон",
#     "last_name": "Смит",
#     "hobbies": ["кузнечное дело", "программирование", "путешествия"],
#     "age": 35,
#     "children": [
#         {
#             "first_name": "Алиса",
#             "age": 5
#         },
#         {
#             "first_name": "Маруся",
#             "age": 3
#         }
#     ]
# }
# print(my_dict)  # выводим весь словарь
# res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)   # dumps, чтобы получить строку байт
# print(res)
# print(f'{res = }')
# print(f'{pickle.DEFAULT_PROTOCOL = }')  # сейчас по умолчанию 4-я версия протокола.

import pickle

# def func(a, b, c):
#     return a + b + c
#
#
# my_dict = {
#     "numbers": [42, 4.1415, 7 + 3j],
#     "functions": (func, sum, max),
#     "others": {True, False, 'Hello world!'},
# }
# with open('my_dict.pickle', 'wb') as f:
#     pickle.dump(my_dict, f)

# ---------------------------
# Десериализация
# ---------------------------
import pickle

# new_dict = pickle.load(f)
# загрузка из бинарного файла и сохранение в объект
#
# new_dict = pickle.loads(data)
# получение объекта из бинарной строки

# import pickle
#
# data = b'\x80\x04\x95\xe3\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\nfirst_name\x94\x8c\x08\xd0\x94\xd0\xb6\xd0\xbe\xd0\xbd\x94\x8c\tlast_name\x94\x8c\x08\xd0\xa1\xd0\xbc\xd0\xb8\xd1\x82\x94\x8c\x07hobbies\x94]\x94(\x8c\x1b\xd0\xba\xd1\x83\xd0\xb7\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xbe\x94\x8c \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd1\x80\xd0\xb0\xd0\xbc\xd0\xbc\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\x94\x8c\x16\xd0\xbf\xd1\x83\xd1\x82\xd0\xb5\xd1\x88\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f\x94e\x8c\x03age\x94K#\x8c\x08children\x94]\x94(}\x94(h\x01\x8c\n\xd0\x90\xd0\xbb\xd0\xb8\xd1\x81\xd0\xb0\x94h\nK\x05u}\x94(h\x01\x8c\x0c\xd0\x9c\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd1\x8f\x94h\nK\x03ueu.'
#
# new_dict = pickle.loads(data)
# print(f'{new_dict = }')

import pickle


# чтобы не вбивать вручную, можно скопировать инфу в файл.
# def func(a, b, c):
#     return a * b * c
#
#
# with open('my_dict.pickle', 'rb') as f:  # открыли для чтения бинарных функций
#     new_dict = pickle.load(f)
# print(f'{new_dict = }')
# print(f'{new_dict["functions"][0](2, 3, 4) = }')

# ------------------
# task
# ------------------

my_dict = {
    "numbers": [42, 4.1415, 7 + 3j],
    "functions": ('functions', sum, max),
    "others": {False, True, 'Hello world!'},
}

res = pickle.dumps(my_dict) # dumps получает на вход словарь и сохраняет в res строку бинарных данных
with open('quest.pickle', 'wb') as f:
    pickle.dump(f'{res = }', f) # получает на запись объект и файловый дискриптор
# в файл будет записан объект двойной сериализации