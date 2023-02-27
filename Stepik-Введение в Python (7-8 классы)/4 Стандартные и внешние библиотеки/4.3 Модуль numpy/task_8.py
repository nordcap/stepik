'''
Среднеквадратичная ошибка
'''

import numpy as np

n = int(input())

matrix1 = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix1.append(temp)

matrix2 = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix2.append(temp)

A = np.array(matrix1)
B = np.array(matrix2)

diff = (A - B) * (A - B)
res = round(diff.sum() / A.size, 2)
print(res)

