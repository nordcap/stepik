'''
Формула №1
'''
import math

point1 = [int(i) for i in input().split()]
point2 = [int(i) for i in input().split()]

a = (point1[0] * point2[0] + point1[1] * point2[1] + point1[2] * point2[2])
b = math.sqrt(point1[0] ** 2 + point1[1] ** 2 + point1[2] ** 2) * math.sqrt(
    point2[0] ** 2 + point2[1] ** 2 + point2[2] ** 2)
rad = math.acos(a / b)
grad = math.degrees(rad)
print(round(grad, 2))
