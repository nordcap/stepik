'''
Вершина параболы
Формат входных данных
На вход программе подаются три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести координаты вершины параболы.
'''

a = int(input())
b = int(input())
c = int(input())

x1 = -b / (2 * a)
x2 = (4 * a * c - b ** 2) / (4 * a)
print(tuple((x1, x2)))
