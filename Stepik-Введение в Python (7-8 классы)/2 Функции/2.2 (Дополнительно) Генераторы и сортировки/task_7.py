'''
Подсчет отрицательных
        Реализуйте сортировку подсчетом, работающую также для отрицательных элементов. Пользоваться функцией sorted() запрещено.
'''

arr = [int(i) for i in input().split()]

j = len(arr) - 1
is_not_ordered = True
while is_not_ordered:
    is_not_ordered = False
    for i in range(j):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            is_not_ordered = True
    j -= 1

print(*arr)
