'''
Суммы четвертей
Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.
Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
'''

n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

sum_top = 0
sum_right = 0
sum_bottom = 0
sum_left = 0

for r in range(n):
    for c in range(n):
        if r < c and r < n - 1 - c:
            sum_top += matrix[r][c]
        if r < c and r > n - 1 - c:
            sum_right += matrix[r][c]
        if r > c and r > n - 1 - c:
            sum_bottom += matrix[r][c]
        if r > c and r < n - 1 - c:
            sum_left += matrix[r][c]

print(f'Верхняя четверть: {sum_top}')
print(f'Правая четверть: {sum_right}')
print(f'Нижняя четверть: {sum_bottom}')
print(f'Левая четверть: {sum_left}')
