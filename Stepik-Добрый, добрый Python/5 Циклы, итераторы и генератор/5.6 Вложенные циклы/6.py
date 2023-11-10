'''
Большой подвиг 6. Вводится список целых чисел в одну строку через пробел. Необходимо выполнить его сортировку выбором по возрастанию (неубыванию).
'''

array = list(map(int, input().split()))

arr_result = []
while len(array) > 0:
    min_elem = min(array)
    array.remove(min_elem)
    arr_result.append(min_elem)

print(*arr_result)
