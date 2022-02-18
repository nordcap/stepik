'''
Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.
'''

n = int(input())
temp = n
sum_digit = 0
count = 0
mul_digit = 1
while n != 0:
    last_digit = n % 10
    sum_digit += last_digit
    count += 1
    mul_digit *= last_digit
    n //= 10
print(sum_digit)
print(count)
print(mul_digit)
print(sum_digit / count)
first_digit = temp // 10 ** (count - 1)
last_digit = temp % 10
print(first_digit)
print(first_digit + last_digit)
