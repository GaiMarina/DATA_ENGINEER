"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""

"""
def make_dict_keys(**kwargs):
    d = {}
    s = set()
    for key, value in kwargs.items():
        try:
            s.add(value)
        except:
            value = str(value)
        d[value] = key
    return d


print(make_dict_keys(a=5, b=6, c=[8, 9]))

"""
# ============================================

def key_parameters_dictionary(**kwargs) -> dict:
    new_kwargs = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, bytearray, dict, frozenset)):
            new_kwargs[str(value)] = key
        else:
            new_kwargs[value] = key

    return new_kwargs


print(key_parameters_dictionary(arg_1=[1, 2], arg_2=234, arg_3='LIST', arg_4={1: 2}))
