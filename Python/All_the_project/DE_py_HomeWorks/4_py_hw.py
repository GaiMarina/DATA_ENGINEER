print('1.\nСоздайте несколько переменных заканчивающихся и не оканчивающихся на «s».\n'
      'Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s\n'
      '(кроме переменной из одной буквы s) на None.Значения не удаляются, \n'
      'а помещаются в одноимённые переменные без s на конце.\n')


def s_object_replace(**kwargs):
    print('Изначальный словарь kwargs: ')
    print(kwargs)
    kwargs_dict = {}
    for obj, m in kwargs.items():
        if obj.endswith('s') and len(obj) > 1:
            kwargs_dict[obj] = None
            obj_2 = obj[:-1]
            kwargs_dict[obj_2] = m
        else:
            kwargs_dict[obj] = m
    print('\nИтоговый словарь: ')
    return kwargs_dict


print(s_object_replace(wars='wars', calls='calls', nos='nos', s='s', abscence='abscence'))

print(f'\n2.\nНапишите функцию для транспонирования матрицы: ')

def matrix_transpose(matrix: list[list]):
    print(f'\nПолученная матрица: ')

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end='\t')
        print()
    print(f'\n')
    transposed_matrix = []
    for lst in zip(*m):
        transposed_matrix.append(list(lst))
    print('Транспонированная матрица: ')
    for r in range(len(transposed_matrix)):
        for c in range(len(transposed_matrix[0])):
            print(transposed_matrix[r][c], end='\t')
        print()
    return transposed_matrix


m = [[1, 3, 4], [78, 5, 4], [2, 8, 9], [2, 8, 9]]
matrix_transpose(m)

print(f'\n3.\nНапишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, \n'
      f'где ключ — значение переданного аргумента, а значение — имя аргумента. \nЕсли ключ не хешируем, '
      f'используйте его строковое представление.')

def key_parameters_dictionary(**kwargs) -> dict:
    print(f'\nДан словарь kwargs: ')
    print(f'{kwargs}\n')
    print(f'\nИтоговый словарь: ')
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

print(f'\n4.\nВозьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. '
      f'Дополнительно сохраняйте все операции поступления и снятия средств в список.')