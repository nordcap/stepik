"""
Поле для игры сапёр представляет собой сетку размером n×mn×m. В ячейке сетки может находиться или
 отсутствовать мина.
Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной,
 указывается число мин, находящихся в соседних ячейках (учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1≤n,m≤1001≤n,m≤100, после чего в n строках
 содержится описание поля в виде последовательности точек '.' и звёздочек '*', где точка означает
  пустую ячейку, а звёздочка − ячейку с миной.

Формат вывода:
nn строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная
символом "*"), при этом число означает количество мин в соседних ячейках поля.
"""
n, m = input().split()
row = int(n)
col = int(m)
matrix = []
c = row
while c > 0:
    h = input()
    matrix.append([i for i in h])
    c -= 1

#matrix = [['.', '.', '*', '.'], ['*', '*', '.', '.'], ['.', '.', '*', '.'], ['.', '.', '.', '.']]
#row, col = 4, 4
result = [[0 for j in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        temp = []  # список с координатами мин

        if matrix[i][j] == '*':
            result[i][j] = '*'
            continue

        for di in range(-1, 2):
            for dj in range(-1, 2):
                if (di == 0 and dj == 0):
                    continue
                ai = i + di
                aj = j + dj
                if row <= ai:
                    continue
                elif ai < 0:
                    continue

                if col <= aj:
                    continue
                elif aj < 0:
                    continue
                if matrix[ai][aj] == '*':
                    temp.append([ai, aj])
        result[i][j] += len(temp)

for line in result:
    for elem in line:
        print(elem, end="")
    print()
