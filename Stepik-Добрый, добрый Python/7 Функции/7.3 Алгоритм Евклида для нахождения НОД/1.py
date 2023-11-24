'''
Большой подвиг 1. Повторите быстрый алгоритм Евклида для нахождения наибольшего общего делителя двух натуральных чисел a и b. В программе необходимо объявить функцию get_nod, которая принимает два аргумента a и b (натуральные числа) и возвращает вычисленное значение НОД(a, b).
'''


def get_nod(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


print(get_nod(15, 121050))
