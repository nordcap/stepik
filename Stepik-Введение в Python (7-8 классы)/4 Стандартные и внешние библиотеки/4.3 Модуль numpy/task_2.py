'''
Число на диагонали
    Программа получает на вход два целых числа N и K. Выведите квадратную матрицу размером N*N, у которой на главной диагонали расположены числа K, а остальные элементы равны 0. Все числа матрицы должны быть целыми.
'''

import numpy as np

array = [int(i) for i in input().split()]
N, K = array[0], array[1]

oneArr = np.eye(N)
result = oneArr * K
print(result.astype(int))
