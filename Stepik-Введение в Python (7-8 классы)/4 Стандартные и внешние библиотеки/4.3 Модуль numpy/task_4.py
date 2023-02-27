'''
Упражнение на индексацию
    Для переданной квадратной матрицы размером N*N, выведите два последних столбца, инвертировав порядок следования строк. Гарантируется, что N >= 2.
'''

import numpy as np

N = int(input())

matrix = []
for i in range(N):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

a = np.array(matrix)
b = a[:, -2:]
print(b[-1::-1, :])
