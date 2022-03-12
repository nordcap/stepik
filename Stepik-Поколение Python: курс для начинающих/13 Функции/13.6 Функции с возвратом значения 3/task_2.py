'''
Площадь и длина
Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
'''

# объявление функции
import math


def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * radius ** 2
    return c, s


print(get_circle(1))
print(get_circle(1.5))
