'''Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся
 строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой
матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной
стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1
Sample Input 2:
1
end
Sample Output 2:
4
'''
matrix = []

while True:
    inp = input().split()
    if inp == ["end"]: break
    lst = [int(i) for i in inp]
    matrix.append(lst)

row = len(matrix)
col = len(matrix[0])

result = [[0 for j in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        temp = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if abs(di) + abs(dj) != 1: continue
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
                temp.append([ai, aj])
        for k in temp:
            result[i][j] += matrix[k[0]][k[1]]

for line in result:
    for elem in line:
        print(elem, end="\t")
    print()
