'''
Три города
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трех городов различны.
'''

name1, name2, name3 = input(), input(), input()
count1 = len(name1)
count2 = len(name2)
count3 = len(name3)

if count1 == min(count1, count2, count3):
    print(name1)
    if count2 == max(count2, count3):
        print(name2)
    else:
        print(name3)
elif count2 == min(count1, count2, count3):
    print(name2)
    if count1 == max(count1, count3):
        print(name1)
    else:
        print(name3)
elif count3 == min(count1, count2, count3):
    print(name3)
    if count1 == max(count1, count2):
        print(name1)
    else:
        print(name2)
