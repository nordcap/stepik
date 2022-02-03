'''
Правильный многоугольник

'''

from math import *

n, a = int(input()), float(input())

S = (n * a ** 2) / (4 * tan(pi / n))
print(S)
