'''
Сложение матриц
Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрицах, затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
'''

arr = [int(i) for i in input().split()]
n = arr[0]
m = arr[1]

matA = []
for _ in range(n):
    temp = [int(num) for num in input().split()]
    matA.append(temp)

input()

matB = []
for _ in range(n):
    temp = [int(num) for num in input().split()]
    matB.append(temp)

for i in range(n):
    for j in range(m):
        print(matA[i][j] + matB[i][j], end=' ')
    print()
