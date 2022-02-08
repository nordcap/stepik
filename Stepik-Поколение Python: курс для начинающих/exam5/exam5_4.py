'''
Римские цифры
Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».

В таблице приведены римские цифры для чисел от 1 до 10.

Число	Римская цифра
1	I
2	II
3	III
4	IV
5	V
6	VI
7	VII
8	VIII
9	IX
10	X
'''

n = int(input())

if 1 <= n <= 10:
    if n == 1:
        print("I")
    elif n == 2:
        print("II")
    elif n == 3:
        print("III")
    elif n == 4:
        print("IV")
    elif n == 5:
        print("V")
    elif n == 6:
        print("VI")
    elif n == 7:
        print("VII")
    elif n == 8:
        print("VIII")
    elif n == 9:
        print("IX")
    else:
        print("X")
else:
    print("ошибка")
