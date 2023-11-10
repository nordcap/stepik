'''
Подвиг 4. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из нулей и, в некоторых позициях, единиц (см. пример ввода ниже). Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и диагонали. То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести ДА, иначе - НЕТ.

P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
'''

import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
'''
heigt = len(lst_in)
width = len(lst_in[0])
# обрамляем матрицу нулями
lst_in.insert(0, [0] * width)
lst_in.append([0] * width)

for i, lst in enumerate(lst_in):
    lst_in[i].insert(0, 0)
    lst_in[i].append(0)

flag = True
for i, row in enumerate(lst_in):
    for j, cell in enumerate(row):
        if lst_in[i][j] == 1:
            for x in range(-1, 2, 2):
                for y in range(-1, 2, 2):
                    if lst_in[i][j] - lst_in[i+x][j+y] == 0:
                        flag = False
'''
height = len(lst_in)
width = len(lst_in[0])
flag = True
for i, row in enumerate(lst_in):
    for j, cell in enumerate(row):
        if i < height - 1 and j < width - 1:
            if cell + lst_in[i + 1][j] + lst_in[i + 1][j + 1] + lst_in[i][j + 1] > 1:
                flag = False

if flag:
    print("ДА")
else:
    print("НЕТ")
