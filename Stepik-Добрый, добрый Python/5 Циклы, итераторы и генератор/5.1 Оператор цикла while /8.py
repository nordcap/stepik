'''
Подвиг 9. Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить, сколько клеток будет через n часов (n - целое положительное число, вводимое с клавиатуры). Считать, что изначально была одна амеба. Результат вывести на экран. Задачу необходимо решить с использованием цикла while.
'''

n = int(input())

arr = [1]
i = 0
while i <= n:
    cur = arr[i] * 2
    arr.append(cur)
    i += 1
    n -= 3
print(arr[-1])
