'''
Контейнеры
        Условие аналогично условию из задачи "Уничтожение популяции". На этот раз ученым необходимо знать, в каких именно контейнерах остались бактерии. Выведите не количество, а их индексы, начиная с 1, разделяя их запятыми.
'''

s = input().split()
time = int(s[0])
max_level = int(s[1])

banks = [int(i) for i in input().split(', ')]

arr = list(map(lambda x: 2 ** time * x, banks))

arr_ind = []
for i, val in enumerate(arr):
    if val <= max_level:
        arr_ind.append(i + 1)
print(*arr_ind, sep=', ')
