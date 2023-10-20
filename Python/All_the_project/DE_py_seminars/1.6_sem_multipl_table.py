
# Таблица умножения
"""
print()
for i in range(11):
    for j in range(5):
        print(f'{j} * {i} = {i * j}    ', end='\t')
    print()
print()
for i in range(11):
    for j in range(5, 10):
        print(f'{j} * {i} = {i * j}    ', end='\t')
    print()
"""

LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4

for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMN):
    for j in range(LOWER_LIMIT, UPPER_LIMIT + 1):
        for k in range(i, i + COLUMN):
            print(f'{k:>2} x {j:>2} = {k * j:>2}', end='\t') # ширина 2 символа, выравниваем вправо
        print()
    print()