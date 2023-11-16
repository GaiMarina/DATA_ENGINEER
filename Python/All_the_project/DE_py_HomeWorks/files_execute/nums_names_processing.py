"""Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.
"""

"""
def multiply_and_safe():
    with open('num_pairs.txt', 'r', encoding='utf-8') as data, \
            open('pseudonyms_generator.txt', 'r', encoding='utf-8') as names, \
            open('result.txt', 'w', encoding='utf-8') as output:
        lines1 = data.readlines()
        lines2 = names.readlines()
        max_lines = max(len(lines1), len(lines2))

        for i in range(max_lines):
            line1 = lines1[i % len(lines1)].strip()     # циклично ходит по файлу от конца на начало.
            line2 = lines2[i % len(lines2)].strip()

            num1, num2 = line1.split(' |')
            num1, num2 = int(num1), float(num2)

            result = num1 * num2

            if result < 0:
                line2 = line2.lower()
                result = abs(result)
            else:
                line2 = line2.upper()
                result = round(result)
            output.write(f'{line2} | {result}\n')


print(multiply_and_safe())
"""


# ------------------------------------------------

def process_files(file_with_numbers: str, file_with_names: str) -> None:
    with (open('num_pairs.txt', 'r', encoding='utf-8') as fnums,
          open('pseudonyms_generator.txt', 'r', encoding='utf-8') as fnames,
          open('result.txt', 'w', encoding='utf-8') as fr):

        fnums.seek(0, 2)    # возврат в конец файла
        file_with_numbers_size = fnums.tell()   # верни текущую позицию (В переменной - позиция курсора в конце файла)
        fnums.seek(0, 0)

        fnames.seek(0, 2)
        file_with_names_size = fnames.tell()
        fnames.seek(0, 0)

        b = 0
        while True:
            row_numbers = fnums.readline()
            row_names = fnames.readline()
            print(f'{row_numbers = } {row_names = }')
            if fnums.tell() >= file_with_numbers_size:
                fnums.seek(0, 0)
            b += 1
            if fnames.tell() >= file_with_names_size:
                fnames.seek(0, 0)
            b += 1
            if b == 2:
                break
