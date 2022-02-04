'''
Арифметические строки
Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.
'''

str1, str2, str3 = input(), input(), input()
num1, num2, num3 = len(str1), len(str2), len(str3)

mi = min(num1, num2, num3)
ma = max(num1, num2, num3)
avg = num1 + num2 + num3 - ma - mi
if ma - avg == avg - mi:
    print("YES")
else:
    print("NO")

