"""Пользователь вводит строку текста.
Подсчитайте сколько раз встречается
каждая буква в строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
Обратите внимание на порядок ключей.
Объясните почему они совпадают или не совпадают в ваших решениях.
"""

# У ГБ выводит со знаками препинания и отдельно заглавные и строчные буквы.

text = input('Введите несколько слов: ')

result_1 = {}
for char in set(text):
    result_1[char] = text.count(char)


result_2 = {}
for char in text:
    if char in result_2:
        result_2[char] += 1
    else:
        result_2[char] = 1

print(f'{result_1 = }\n{result_2 = }')


#========================================
"""
text = input('Введите текст: ')
dictionary = dict()
if text != text.lower():
    text = sorted(text.lower())
draft = ''
for char in text:
    if char.isalpha():
        draft += char

for letter in set(draft):
    counter = 0
    for i in draft:
        if letter == i:
            counter += 1
    else:
        key = dictionary.setdefault(letter, counter)

print(dict(sorted(dictionary.items())))
"""
#=======================================
"""
text = input('Введите текст: ')
dictionary = dict()
if text != text.lower():
    text = text.lower()
draft = ''
for char in text:
    if char.isalpha():
        draft += char

for letter in set(draft):
    key = dictionary.setdefault(letter, draft.count(letter))

print(dict(sorted(dictionary.items())))

"""
