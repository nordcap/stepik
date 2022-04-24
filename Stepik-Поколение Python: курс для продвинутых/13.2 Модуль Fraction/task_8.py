'''
Упорядоченные дроби
На вход программе подается натуральное число nn. Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между 00 и 11, знаменатель которых не превосходит nn.

Формат входных данных
На вход программе подается натуральное число n, \, n > 1n,n>1.

Формат выходных данных
Программа должна вывести ответ на задачу.

Примечание. Возможно вам потребуется функция gcd(), которая позволяет находить наибольший общий делитель (НОД) двух чисел. Функция реализована в модуле math.
'''

from fractions import Fraction
from math import gcd

n = int(input())

arr_numerators = [i for i in range(1, n)]
arr_denominators = [i for i in range(2, n + 1)]
arr_out = []
for i in arr_numerators:
    for j in arr_denominators:
        if gcd(i, j) == 1 and Fraction(i, j) < 1:
            arr_out.append(Fraction(i, j))

for elem in sorted(arr_out):
    print(elem)
