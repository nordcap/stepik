'''
Хитрая сумма
    Вводится натуральное число n. Для этого числа вычислите n-ое число Фибоначчи и выведите сумму этого числа и его факториала. Вычисление числа Фибоначчи и факториала вынесите в отдельные функции factorial(n) и fib(n). Считайте первое число Фибоначчи равным единице.
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


n = int(input())
print(fib(n) + factorial(n))
