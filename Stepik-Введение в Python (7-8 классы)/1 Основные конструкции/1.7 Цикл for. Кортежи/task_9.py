'''
Сумма квадратов
﻿  Посчитайте сумму квадратов всех чисел, находящихся в полуинтервале [a, b) или [b, a), и выведите ее на экран.
'''

a = int(input())
b = int(input())
minimum = None
maximum = None
if a > b:
    minimum = b
    maximum = a
elif a < b:
    minimum = a
    maximum = b

sum = 0
for i in range(minimum, maximum):
    sum += i ** 2

print(sum)
