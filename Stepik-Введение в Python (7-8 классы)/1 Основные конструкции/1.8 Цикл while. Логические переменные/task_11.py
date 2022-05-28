'''
Olympiadnik Starter Pack
  Попробуйте совместить изученные алгоритмы, чтобы решить такую составную задачу: найдите НОД двух чисел – максимума и минимума последовательности и выведите YES, если это простое число и NO, если число составное.

  Формат ввода: число n, затем n строк, образующих числовую последовательность

  Формат вывода: число – НОД максимума и минимума последовательности, а на следующей строке – слово YES или NO.

'''


def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_simple(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


n = int(input())
x = int(input())
maximim = x
minimum = x

for _ in range(n - 1):
    x = int(input())
    if x > maximim:
        maximim = x
    if x < minimum:
        minimum = x

res = nod(maximim, minimum)
print(res)
if is_simple(res) and res != 1:
    print("YES")
else:
    print("NO")
