"""
Напишите программу, вычисляющую следующее состояние поля для Game of life.

Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с противоположного конца (поле представляет собой тор).

Формат ввода:

На первой строке указаны два целых числа через пробел -- высота и ширина поля.
В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую.

Формат вывода:
Следующее состояние поля, используя те же обозначения, что использовались на вводе.
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
'''
matrix = [['.', '.', '.', '.', '.'],
          ['.', '.', 'X', '.', '.'],
          ['.', '.', '.', 'X', '.'],
          ['.', 'X', 'X', 'X', '.'],
          ['.', '.', '.', '.', '.'],
          ]
matrix = [['.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.'],
          ['.', 'X', 'X', 'X', '.'],
          ['.', '.', '.', '.', '.'],
          ]
matrix = [['.', '.', '.', 'X', 'X', '.'],
          ['.', 'X', 'X', '.', '.', '.'],
          ['.', '.', 'X', '.', '.', '.'],
          ['X', 'X', '.', '.', '.', '.'],
          ['X', '.', '.', 'X', 'X', '.'],
          ]
row, col = 5, 6 '''
result = [['.' for j in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        lst_life = []  # список с координатами где есть жизнь
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if (di == 0 and dj == 0):
                    continue
                ai = i + di
                aj = j + dj
                if row <= ai:
                    ai = 0
                elif ai < 0:
                    ai = row - 1

                if col <= aj:
                    aj = 0
                elif aj < 0:
                    aj = col - 1
                if matrix[ai][aj] == 'X':
                    lst_life.append([ai, aj])
        count_life = len(lst_life)
        if matrix[i][j] == '.' and count_life == 3:
            result[i][j] = 'X'
        elif matrix[i][j] == 'X' and (count_life == 2 or count_life == 3):
            result[i][j] = 'X'
        elif matrix[i][j] == 'X' and (
                        count_life < 2 or count_life > 3):  # данное условие можно опустить из-за начального заполнения матрицы
            result[i][j] = '.'

for line in result:
    for elem in line:
        print(elem, end="")
    print()
