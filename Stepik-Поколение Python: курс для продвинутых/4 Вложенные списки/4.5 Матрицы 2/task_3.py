'''
Обмен столбцов
Напишите программу, которая меняет местами столбцы в матрице.

Формат входных данных
На вход программе на разных строках подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем элементы матрицы построчно через пробел, затем числа ii и jj — номера столбцов, подлежащих обмену.

Формат выходных данных
Программа должна вывести указанную таблицу с замененными столбцами.
'''

n = int(input())
m = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

arr = [int(k) for k in input().split()]
i, j = arr[0], arr[1]
for r in range(n):
    matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
