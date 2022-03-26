'''
Максимальный в области 2 🌶️
'''

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

max_matrix = -999
for r in range(n):
    for c in range(n):
        if ((r == c or r + c + 1 == n) or (r > c and r < n - 1 - c) or (r < c and r > n - 1 - c)):
            if matrix[r][c] > max_matrix:
                max_matrix = matrix[r][c]
print(max_matrix)
