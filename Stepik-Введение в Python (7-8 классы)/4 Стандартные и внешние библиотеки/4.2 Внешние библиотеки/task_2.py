'''
Накопление значений
    С клавиатуры вводятся числа N и M, затем N строк с M целыми числами. Умножьте элементы каждой строки на номер этой строки, начиная с 1, и выведите массив из сумм соответствующих элементов всех строк.
'''
import numpy as np

a = [int(i) for i in input().split()]
N = a[0]
M = a[1]

result = np.array([0] * M)
for i in range(1, N + 1):
    array = np.array([int(i) for i in input().split()])
    row = array * i
    result = result + row

print(result)
