'''Выведите таблицу размером n×n,  заполненную числами от 1 до n**2 по спирали, выходящей из левого верхнего угла и
закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''
sizeX = int(input())  # размер массива по горизонтали
sizeY = sizeX  # размер массива по вертикали
array = [[0 for i in range(sizeX)] for j in range(sizeY)]

Summ = sizeX * sizeY  # произведение ширины на высоту, нужно для устранения ошибки (см. Далее)

# y - текущая сторона (0 - вверх, 1 - право, 2 - ...)
# x - собственно позиция внутри массива


CorrectX = 0  # переменная, которая отвечает за автоматическое декриментирование
CorrectY = 0
Count = 1  # переменная, которая отвечает за текущую цыфру внутри массива

while sizeY > 0:
    for y in range(4):
        for x in range(sizeY if sizeX < sizeY else sizeX):
            if y == 0 and x < sizeX - CorrectX and Count <= Summ:
                array[y + CorrectY][x + CorrectX] = Count
                Count += 1
            if y == 1 and x < sizeY - CorrectY and x != 0 and Count <= Summ:
                array[x + CorrectY][sizeX - 1] = Count
                Count += 1
            if y == 2 and x < sizeX - CorrectX and x != 0 and Count <= Summ:
                array[sizeY - 1][sizeX - (x + 1)] = Count
                Count += 1
            if y == 3 and x < sizeY - (CorrectY + 1) and x != 0 and Count <= Summ:
                array[sizeY - (x + 1)][CorrectY] = Count
                Count += 1

    sizeY -= 1
    sizeX -= 1
    CorrectX += 1
    CorrectY += 1

for line in array:
    for elem in line:
        print(elem, end="\t")
    print()
