'''
Подвиг 8. Вводятся целые числа в одну строку через пробел. На их основе формируется кортеж. Необходимо найти и вывести все индексы неуникальных (повторяющихся) значений в этом кортеже. Результат отобразите в виде строки чисел, записанных через пробел.
'''

t = tuple(list(map(int, input().split())))
lst = list(t)
res = []
for ind, val in enumerate(lst):
    if lst.count(val) > 1:
        res.append(ind)

print(*res)
