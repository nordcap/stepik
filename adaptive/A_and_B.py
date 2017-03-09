"""
Задача на работу со строками.

Многим знакома детская загадка:

А и Б сидели на трубе.
А упало, Б пропало.
Что осталось на трубе?

Перевод, (какой я смог найти):

A and B sat in the tree.
A had fallen, B was stolen.
What's remaining in the tree?

Напишите программу, которая считывает два имени и выводит стихотворение, в котором вместо A и B
используются эти имена.

Формат ввода:
Два имени, разделённых переносом строки. Первое имя должно заменять A, второе −− B.

Формат вывода:
Три строки стихотворения с заменёнными A и B.
"""

A = input().strip()
B = input().strip()

str = """A and B sat in the tree.
A had fallen, B was stolen.
What's remaining in the tree?"""

str_A = str.replace("A", A)
str_B = str_A.replace("B", B)
arr = str_B.split("\n")
for i in arr:
    print(i)
