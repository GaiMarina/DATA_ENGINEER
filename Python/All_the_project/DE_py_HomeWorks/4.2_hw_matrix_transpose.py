"""Напишите функцию для транспонирования матрицы
"""


def matrix_transpose(m):
    new = []
    for i in range(len(m[0])):
        new.append([])
    for i in range(len(m)):
        for j in range(len(m[i])):
            new[j].append(m[i][j])
    return new


print(matrix_transpose([[1, 2], [3, 4], [5, 6]]))


# ==============================================
"""
def matrix_transpose(matrix: list[list]):
    print(f'\nПолученная матрица: ')

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end='\t')
        print()
    print(f'\n')
    transposed_matrix = []
    for lst in zip(*m):
        transposed_matrix.append(list(lst))
    print('Транспонированная матрица: ')
    for r in range(len(transposed_matrix)):
        for c in range(len(transposed_matrix[0])):
            print(transposed_matrix[r][c], end='\t')
        print()
    return transposed_matrix


m = [[1, 3, 4], [78, 5, 4], [2, 8, 9], [2, 8, 9]]
matrix_transpose(m)

"""