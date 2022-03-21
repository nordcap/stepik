'''
Треугольник Паскаля 2
На вход программе подается натуральное число nn. Напишите программу, которая выводит первые nn строк треугольника Паскаля.
'''

from math import factorial


def paskal(n):
    arr = [0] * (n + 1)
    for m in range(n + 1):
        arr[m] = int(factorial(n) / (factorial(m) * factorial(n - m)))
    return arr


n = int(input())

for i in range(n):
    print(*paskal(i))
