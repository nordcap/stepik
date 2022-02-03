'''
Евклидово расстояние

'''
from math import *

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
s = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(s)
