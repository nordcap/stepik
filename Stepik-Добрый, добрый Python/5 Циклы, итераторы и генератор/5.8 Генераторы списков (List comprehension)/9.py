'''
 Вводится список в формате:

<город 1> <численность населения 1> <город 2> <численность населения 2> ... <город N> <численность населения N>

Необходимо с помощью list comprehension сформировать список lst, содержащий вложенные списки из пар:

<город> <численность населения>

Численность населения - целое число в тыс. человек. Вывести результат на экран в виде списка командой:

print(lst)
'''

cities = input().split()
count_man = [int(cities[i]) for i in range(len(cities)) if i % 2 != 0]
city = [cities[i] for i in range(len(cities)) if i % 2 == 0]
res = [[city[i], count_man[i]] for i in range(len(city))]
print(res)
