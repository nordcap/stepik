'''
Индексы минимального
    Выведите сумму индексов минимального числа последовательности. Ряд чисел вводится с клавиатуры, числа разделяются запятыми. Индексация начинается с нуля.
'''

arr = [int(i) for i in input().replace(' ', '').split(',')]
m = min(arr)
count = arr.count(m)
sum_ind = 0
start_index = -1
for k in range(count):
    start_index = arr.index(m, start_index + 1)
    sum_ind += start_index
print(sum_ind)
