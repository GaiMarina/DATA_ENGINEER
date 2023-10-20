"""Пользователь вводит строку текста. Вывести каждое слово с новой строки.
Слова нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки."""

texts = sorted(input('Введите несколько слов: ').split())

max_len = 0
for word in texts:
    if len(word) > max_len:
        max_len = len(word)

for i, word in enumerate(texts, start=1):
    print(f'{i}. {word:>{max_len}}')

#===========================================
"""
texts = sorted(input('Введите несколько слов: ').split())
max_word = 'a'
for i in texts:
    max_word = i if len(i) > len(max_word) else max_word
    length = len(max_word) + 1

for n, item in enumerate(texts, start=1):
    print(f'{n}{item:>{length}}')
"""