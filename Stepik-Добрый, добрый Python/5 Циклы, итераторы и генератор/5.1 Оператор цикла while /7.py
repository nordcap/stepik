'''
Подвиг 8. Последовательность Фибоначчи образуется так: первые два числа равны 1 и 1, а каждое последующее равно сумме двух предыдущих. Имеем такую последовательность чисел: 1, 1, 2, 3, 5, 8, 13, ... Постройте последовательность Фибоначчи длиной n (n вводится с клавиатуры). Результат отобразите в виде строки полученных чисел, записанных через пробел. Программу реализовать при помощи цикла while.
'''

n = int(input())

arr = [1, 1]
i = 1
while i < n - 1:
    cur = arr[i - 1] + arr[i]
    arr.append(cur)
    i += 1
print(*arr)
