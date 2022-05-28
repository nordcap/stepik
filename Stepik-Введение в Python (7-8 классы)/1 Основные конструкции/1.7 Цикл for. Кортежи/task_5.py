'''
Сумма ряда
  Посчитайте сумму всех чисел на полуинтервале [a; b) или [b; a), в зависимости от того, какое число больше.
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
    sum += i
print(sum)
