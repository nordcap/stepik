'''
Формула №2
'''

from math import *

arr = [int(i) for i in input().split()]
a = arr[0]
b = arr[1]

numerator = factorial(floor(b / a)) + a ** (b * pi)
denominator = log2(a) * sqrt(a / b) * cos(b + exp(a))
F = ceil(numerator / denominator)
print(F)
