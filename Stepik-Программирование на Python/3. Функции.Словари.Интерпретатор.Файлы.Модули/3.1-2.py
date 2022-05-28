'''Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
st = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

Функция не должна осуществлять ввод/вывод информации.
'''
lst = [1, 2, 3, 3, 5, 4, 5, 7, 6, 10]


def modify_list(l):
    global lst

    def odd(elem):
        '''удаляем все нечетные значения (те оставляем все четные)'''

        return elem % 2 == 0

    def even(elem):
        '''все четные (оставшиеся) нацело делим на 2'''
        return elem // 2

    arr = list(filter(odd, l))
    lst = list(map(even, arr))

    return


print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)
