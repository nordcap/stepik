'''
На вход подается строка. Затем подается буква. Ваша задача - определить индекс второго﻿ вхождения этой буквы в строку.

Если этой буквы нет или она одна, верните -1.

Формат входных данных: Строка и буква, на разных строках.

Формат выходных данных:  Число

Sample Input 1:

harry potter
t
Sample Output 1:

9
Sample Input 2:

hermione granger
y
Sample Output 2:

-1
'''

str_inp = input()
a = input()

if str_inp.count(a) == 1 or str_inp.count(a) == 0:
    print("-1")
else:
    pos1 = str_inp.find(a)
    pos2 = str_inp.find(a, pos1+1)
    print(pos2)

