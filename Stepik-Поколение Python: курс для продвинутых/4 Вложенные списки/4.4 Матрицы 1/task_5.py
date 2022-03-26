'''
Максимальный в области 1
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
'''

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

max_matrix = -999
for r in range(n):
    for c in range(n):
        if r >= c:
            if matrix[r][c] > max_matrix:
                max_matrix = matrix[r][c]

print(max_matrix)
