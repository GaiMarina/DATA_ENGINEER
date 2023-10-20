"""Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""
text = 'Всем привет! Повторите, пожалуйста, задание!!!'


def words_output(text_line: str):
    draft = ''
    for char in text_line:
        if char.isalpha():
            draft += char
        else:
            draft += ' '
    draft = sorted(draft.split())
    max_length = len(max(draft, key=lambda x: len(x))) + 1

    for num, value in enumerate(sorted(draft), start=1):

        print(f'{num}.{value:>{max_length}}')

words_output(text)
