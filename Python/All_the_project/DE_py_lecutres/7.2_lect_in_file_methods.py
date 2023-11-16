# Запись в файл

# res = f.write(text)
# f.writelines('\n'.join(text))
# print(text, file=f)

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in text:
#         res = f.write(f'{line}\n')          # .write() запишет в файл и сохранит в переменную
#         print(f'{res = }\n{len(line) = }')  # print() выведет на консоль.

#------------------------------
# Методы
#------------------------------

# f.tell() выводит позицию на которой находится курсор.

# seek(offset, whence=0)
# offset - смещение относительно начальной точки (отриц. или полож.значение)
# whence - выбор начальной точки (0, 1 или 2) whence=0 - отсчет от начала файла; =1 - от текущей точки; =2 - от конца.
#       whence - доступно только в двоичном режиме (символ b в параметре mode)
# seek(offset=0, whence=2) - открыли текстовый файл и хотим сразу перейти в конец файла.

# truncate(size=None) !!! Если не передать size, потеряется все, что от текущего нахождения курсора и до конца.
#       Если задать size, останется все от начала до size, от size до конца - удалится..
"""
last = before = 0
text = ['a;slkdfj', 'a;lskdjf', 'a;slkdjf']
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before  = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
"""

# EX:
start = 10
stop = 100
with open('data.bin', 'bw+') as f:
    for i in range(start, stop + 1):
        f.write(str(i).encode('utf-8'))
        if i % 3 == 0:
            f.seek(-2, 1)
    f.truncate(stop)
    f.seek(0)
    res = f.read(start)
    print(res.decode('utf-8'))
