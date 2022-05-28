'''
Вывести чётные
  Необходимо вывести все четные числа на отрезке [a; a * 10].
'''
a = int(input())
if a % 2 == 0:
    print(tuple(range(a, a * 10 + 1, 2)))
else:
    print(tuple(range(a + 1, a * 10 + 1, 2)))
