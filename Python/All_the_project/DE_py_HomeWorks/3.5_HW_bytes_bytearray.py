# bytes - НЕ изменяемые
# bytearray - изменяемые

# метод .encode() для представления набора данных в виде байт
"""
text_en = 'Hello World!'
res = text_en.encode('utf-8')
print(res, type(res))

text_en = 'Привет, мир!'
res = text_en.encode('utf-8')
print(res, type(res))
"""

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = }\n{y = }')