'''
Подвиг 4. Вводится список в виде целых чисел в одну строку через пробел. Необходимо сначала сформировать список на основе введенной строки, а затем, каждое значение этого списка изменить, возведя в квадрат. Отобразить результат на экране в виде строки полученных чисел, записанных через пробел. Программу следует реализовать с использованием функции enumerate.
'''

array = list(map(int, input().split()))
for i, d in enumerate(array):
    array[i] = d ** 2

print(*array)
