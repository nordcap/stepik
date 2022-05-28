'''
Построение простых
   Вводится натуральное число n. Выведите количество простых чисел на отрезке [2; n]. Число n не превышает 10^5.
'''
def is_simple(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


n = int(input())

count_simple = 0
for current in range(2, n + 1):
    if is_simple(current):
        count_simple += 1
print(count_simple)
