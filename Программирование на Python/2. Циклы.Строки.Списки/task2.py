'''Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно). На вход программе передаётся положительное целое число
n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел,
записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
Sample Input:
7
Sample Output:
1 2 2 3 3 3 4
'''
n = int(input())
i = 1
str = []
arr = []

while i <= n:
    temp = [i] * i
    str += temp
    k = len(str)
    if n <= k:
        arr = str[0:n]
        break
    i += 1

for i in arr:
    print(i, end=" ")
