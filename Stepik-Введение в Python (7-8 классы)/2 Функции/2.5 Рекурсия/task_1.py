'''
Функция Аккермана
    Реализуйте функцию Аккермана, которая определяется рекурсивно для неотрицательных целых чисел m и n следующим образом:


'''


def akkerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akkerman(m - 1, 1)
    elif m > 0 and n > 0:
        return akkerman(m - 1, akkerman(m, n - 1))


n, m = int(input()), int(input())

print(akkerman(m, n))
