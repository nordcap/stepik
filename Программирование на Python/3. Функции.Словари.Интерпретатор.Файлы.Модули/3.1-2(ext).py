"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации.

"""
lst = [1, 2, 3, 3, 5, 4, 5, 7, 6, 6]


def modify_list(l):
    def odd(elem):
        '''удаляем все нечетные значения (те оставляем все четные)'''
        return elem % 2 == 0

    def even(elem):
        '''все четные (оставшиеся) нацело делим на 2'''
        return elem // 2

    arr = l[:]

    arr = list(filter(odd, arr))
    arr = list(map(even, arr))

    del l[:]

    for i in range(len(arr)):
        l.append(arr[i])

    return


print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)  # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
