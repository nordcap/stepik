'''
Большой подвиг 7. Вводится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку по возрастанию (неубыванию) методом всплывающего пузырька.
'''

array = list(map(int, input().split()))

for i in range(len(array) - 1):
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(*array)
