'''
Подвиг 3. Объявите функцию с именем get_even, которая принимает произвольное количество чисел в качестве аргументов и возвращает список, составленный только из четных переданных значений.

Функцию выполнять не нужно, только определить.
'''


def get_even(*args):
    return [x for x in args if x % 2 == 0]


l = list(map(int, input().split()))

print(*get_even(*l))
