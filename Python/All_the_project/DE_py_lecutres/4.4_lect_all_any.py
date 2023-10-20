# all(iterable)
# ----------------------------------------
# Возвращает истину, если все элементы послед-ти являются истиной

def all_(iterable):
    for element in iterable:
        if not element:
            return False
    return True


numbers = [-56, 24, 13]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('Есть отрицательные и/или нулевые элементы.')


# any(iterable)
# ----------------------------------------
# Возвращает истину, если хотя бы один - истина

def any_(iterable):
    for element in iterable:
        if element:
            return True
    return False


numbers = [-56, 24, 13]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')
