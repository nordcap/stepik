"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки
сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

Sample Input 1:
8
2
14
Sample Output 1:
14
2
8
Sample Input 2:
23
23
21
Sample Output 2:
23
21
23

"""
a = int(input())
b = int(input())
c = int(input())

if max(a, b, c) == a:
    mx = a
    if min(b, c) == b:
        mn = b
        avg = c
    else:
        mn = c
        avg = b
elif max(a, b, c) == b:
    mx = b
    if min(a, c) == a:
        mn = a
        avg = c
    else:
        mn = c
        avg = a
elif max(a, b, c) == c:
    mx = c
    if min(a, b) == a:
        mn = a
        avg = b
    else:
        mn = b
        avg = a

print(mx)
print(mn)
print(avg)
