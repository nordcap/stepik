'''
Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().

def product_of_odds(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result
'''
from functools import reduce


def product_of_odds(data):
    result_filter = list(filter(lambda i: i % 2 == 1, data))
    return reduce(lambda x, y: x * y, result_filter, 1)
