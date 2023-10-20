"""Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию."""

text = 'Всем привет! Повторите, пожалуйста, задание!!!'


def every_char_unicode(txt: str):
    new_str = list(set([ch for ch in text if ch != ' ']))
    return sorted([ord(char) for char in new_str], reverse=True)


print(every_char_unicode(text))
