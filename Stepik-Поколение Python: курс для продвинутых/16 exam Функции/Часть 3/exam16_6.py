'''
Напишите функцию call(), которая принимает произвольную функцию и аргументы для неё и делает вызов переданной функции, возвращая ее значение.
'''


def call(func, *args):
    return func(*args)


def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))
