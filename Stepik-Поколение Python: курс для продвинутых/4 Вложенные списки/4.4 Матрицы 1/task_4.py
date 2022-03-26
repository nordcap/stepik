'''
Больше среднего
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
'''


def convert_to_int(arr):
    for i, elem in enumerate(arr):
        arr[i] = int(elem)
    return arr


n = int(input())
matrix = [convert_to_int(input().split()) for _ in range(n)]

for r in range(n):
    count = 0
    p = sum(matrix[r]) / len(matrix[r])
    for c in range(n):
        if matrix[r][c] > p:
            count += 1
    print(count)
