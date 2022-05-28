'''Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, которая выводит
все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
Sample Input 1:
5 8 2 7 8 8 2 4
8
Sample Output 1:
1 4 5
Sample Input 2:
5 8 2 7 8 8 2 4
10
Sample Output 2:
Отсутствует
'''
lst = [int(i) for i in input().split()]
x = int(input())
pos = []
n = 1
begin = 0
count = lst.count(x)

if count == 0:
    print("Отсутствует")
else:
    while n <= count:
        begin = lst.index(x, begin)
        pos.append(begin)
        begin += 1
        n += 1
print(" ".join(str(i) for i in pos))
