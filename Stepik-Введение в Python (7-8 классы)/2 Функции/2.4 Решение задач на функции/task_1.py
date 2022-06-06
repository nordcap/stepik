'''
Сумма факториалов
    С клавиатуры вводятся числа a и b, b > a. Найдите сумму факториалов чисел из диапазона [a; b]. Для вычисления факториала реализуйте функцию factorial(n).
'''


# используйте функцию factorial(n)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


a, b = int(input()), int(input())
s = 0
for n in range(a, b + 1):
    s += factorial(n)


print(s)
