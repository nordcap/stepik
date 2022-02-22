'''
Все вместе 2
Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно).
Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.
'''

n = int(input())
count_3 = 0
last = n % 10
count_last = 0
count_even = 0
summ_more_5 = 0
mul_more_7 = 1
count_0_5 = 0
while n != 0:
    last_digit = n % 10
    if last_digit == 3:
        count_3 += 1
    if last_digit == last:
        count_last += 1
    if last_digit % 2 == 0:
        count_even += 1
    if last_digit > 5:
        summ_more_5 += last_digit
    if last_digit > 7:
        mul_more_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        count_0_5 += 1
    n //= 10
print(count_3)
print(count_last)
print(count_even)
print(summ_more_5)
print(mul_more_7)
print(count_0_5)
