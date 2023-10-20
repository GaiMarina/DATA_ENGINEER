"""Три друга взяли вещи в поход.
Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы: Какие вещи взяли все три друга
Какие вещи уникальны, есть только у одного друга
Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей.
"""

hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметичка"),
}

# Как можно пересечение множеств сделать лаконично!
# вещи, которые взяли все 3 друга:
common_items = set.intersection(*[set(hike[friend]) for friend in hike])
print(common_items)


#=====================================================
"""
hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметичка"),
}

at_all = set()
for values in hike.values():
    for value in values:
        at_all.add(value)  # {'спальник', 'топор', 'вода', 'дрова', 'еда', 'спички', 'косметичка'}
print(f'Полный список вещей: {at_all = }')

unique = {}
for master_key, master_values in hike.items():
    for slave_key, slave_values in hike.items():
        if master_key != slave_key:  # пары неодинаковых ключей
            if unique.get(master_key):
                unique[master_key] -= set(slave_values)
            else:
                unique[master_key] = set(master_values) - set(slave_values)
print(f'Уникальные вещи: {unique = }')

duplicates = set(at_all)
for value in unique.values():
    duplicates -= value
print(f'Дублирующие вещи: {duplicates = }')

for key, value in hike.items():
    print(f'У {key} отсутствует {(set(value) ^ duplicates) - set(unique[key])}, но есть у остальных')
"""
# ==========================================
"""
INPUT = 'н'
RESULT = 'р'
ALL_LIST = 'с'
CONTITNUE = 'п'
dictionary = dict()
set_of_things = set()
all_the_things = []
counter = 0
joint_list = []
name_list = []

while True:
    print('-' * 20)
    result = input(f'н - ввести нового друга;\nр - перейти к анализу;\n'
                   f'в - выйти\nс - посмотреть весь список\n')
    print('-' * 20)

    if result == 'н':
        key_name = input('Введите имя друга: ')
        name_list.append(key_name.strip())
        things_list = input('Введите вещи, чтобы взять с собой через пробел: ').strip().lower().split()
        counter += 1
        dictionary[key_name] = tuple(things_list)
        set_of_things = set_of_things.union(set(things_list))
        all_the_things.extend(list(set(things_list)))
        max_value = max(set_of_things, key=len)
        continue
    elif result == 'с':
        for keys, values in dictionary.items():
            print(f'{keys}:', end='\t')
            for things in values:
                print(things, end=' ')
            print()
        continue
    elif result == 'р':
        for things in set_of_things:
            if all_the_things.count(things) == counter:
                joint_list.append(things)
        print(f'Все {counter} друга взяли {", ".join(joint_list)}') if joint_list else \
            print('Нет вещей, которые бы взял каждый из друзей.')
        # print(all_the_things, counter, joint_list)
        while True:
            name = input('Введите имя друга в списке: ')
            # print(name_list)
            if name not in name_list:
                print(f'Имени {name} нет в списке. Попробуйте еще раз: ')
                continue
            else:
                break

        f = 0
        for keys, values in dictionary.items():
            if keys == name:
                continue
            elif keys != name and f == 0:
                friends_set = set(dictionary[keys])
                f = 1
            elif keys != name and f == 1:
                friends_set = friends_set.union(set(dictionary[keys]))
                # print(friends_set)
        for keys, values in dictionary.items():
            if keys == name:
                result = list(set(dictionary[keys]).difference(friends_set))

        print(f'Только {name} взял(а): {", ".join(result)}.') if result else \
            print(f'Нет таких вещей, которые взял(а) бы только {name}')

        name_1, name_2, name_3 = dictionary.keys()
        # print(len(set(dictionary[name_1]).intersection(set(dictionary[name_2]))))
        # print(name_1, name_2, name_3)
        print(f'{name_1} и {name_2} взяли '
              f'{list(set_of_things.difference(set(dictionary[name_3])))}, а {name_3} не взял(взяла)')
        print(f'{name_1} и {name_3} взяли '
              f'{list(set_of_things.difference(set(dictionary[name_2])))}, а {name_2} не взял(взяла)')
        print(f'{name_2} и {name_3} взяли '
              f'{list(set_of_things.difference(set(dictionary[name_1])))}, а {name_1} не взял(взяла)')
    elif result == 'в':
        quit('Пока!')

"""