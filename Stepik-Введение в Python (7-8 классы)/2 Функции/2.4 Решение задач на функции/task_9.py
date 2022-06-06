'''
Циклический сдвиг
    Реализуйте алгоритм циклического сдвига значений списка на указанное число шагов n. Если n – положительное число, нужно сдвинуть все элементы списка на n вправо, а элементы, вышедшие за границу списка, переместить в начало. Если n – отрицательное число, нужно сдвинуть все элементы списка на n влево, а элементы, вышедшие за границу списка, переместить в конец. Для этого определите функцию shift_list(), которая принимает на вход список чисел и шаг сдвига и возвращает измененный список. Кроме функции ничего писать не нужно.
'''


def shift_list(lst, shift):
    # diff = 0
    if abs(shift) > len(lst):
        diff = shift % len(lst)
    else:
        diff = shift
    if diff > 0:
        cut_arr = lst[-diff:]
        cut_arr.extend(lst[:len(lst) - diff])
        return cut_arr

    else:
        cut_arr = lst[:-diff]
        out = lst[-diff:]
        out.extend(cut_arr)
        return out


arr = [int(i) for i in input().split()]
shift = int(input())

print(*shift_list(arr, shift))
