"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""


def key_parameters_dictionary(**kwargs) -> dict:
    new_kwargs = {}
    for key, value in kwargs.items():
        if type(value) == list or \
                type(value) == frozenset or \
                type(value) == bytearray or \
                type(value) == dict:
            new_kwargs[str(value)] = key
        else:
            new_kwargs[value] = key

    return new_kwargs


print(key_parameters_dictionary(arg_1=[1, 2], arg_2=234, arg_3='LIST', arg_4={1: 2}))
