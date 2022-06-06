"""
Напишите программу, которая находит все позиции вхождения подстроки в строку.
Формат ввода:
На первой строке содержится исходная строка, на второй строке ввода указана подстрока, позиции которой требуется найти. Строки состоят из символов латинского алфавита.

Формат вывода:
Строка, содержащая индексы (индексация начинается с нуля) вхождения подстроки в строку, разделённые пробелом или число -1 в случае, когда подстрока не найдена.

Sample Input 1:
abacabadaba
aba
Sample Output 1:
0 4 8
Sample Input 2:
aaaa
aa
Sample Output 2:
0 1 2
Sample Input 3:
abc
d
Sample Output 3:
-1
"""

str = input()
substr = input()
lst_pos = []

for i in range(len(str)):
    pos = str.find(substr, i)
    if pos == -1:
        break
    if not pos in lst_pos:
        lst_pos.append(pos)

if len(lst_pos) > 0:
    for i in lst_pos:
        print(i, end=" ")
else:
    print(-1)
