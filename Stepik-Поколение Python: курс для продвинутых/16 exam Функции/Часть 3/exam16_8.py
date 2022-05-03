'''
Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций (+, -, *, /) и возвращает функцию двух аргументов для соответствующей операции.
'''
from operator import *


def arithmetic_operation(op):
    if op == '+':
        return add
    elif op == '-':
        return sub
    elif op == '*':
        return mul
    elif op == '/':
        return truediv


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
