'''
Сумма на диагонали
    Вводится квадратная матрица размером N*N. Выведите сумму двух характеристик массива:

    1. Сумма четных элементов главной диагонали

    2. Произведение всех ненулевых элементов главной диагонали

    Примечание: узнайте, как работает функция np.diagonal().
'''
import numpy as np

N = int(input())

matrix = []
for i in range(N):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

A = np.diagonal(np.array(matrix))
# 1.Сумма четных элементов главной диагонали
sum_odd = A[A % 2 == 0].sum()
# 2. Произведение всех ненулевых элементов главной диагонали
mul_non_zeros = A[A != 0].prod()

print(sum_odd + mul_non_zeros)
