# Домашняя работа по уроку "Функции в Python.Функция с параметром"

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


def print_matrix(matrix):
    for i in matrix:
        print(i)


matrix_1 = get_matrix(2, 2, 10)
matrix_2 = get_matrix(3, 5, 42)
matrix_3 = get_matrix(4, 2, 13)

print_matrix(matrix_1)
print_matrix(matrix_2)
print_matrix(matrix_3)
