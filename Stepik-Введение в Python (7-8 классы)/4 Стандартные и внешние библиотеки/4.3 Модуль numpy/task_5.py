'''
Сумма столбца
    Вводится квадратная матрица размером N*N, затем число M. Вычислите сумму всех элементов столбца с индексом M (индексация начинается с 0).
'''

import numpy as np

N = int(input())

matrix = []
for i in range(N):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

M = int(input())

a = np.array(matrix)
print(a[:, M].sum())
