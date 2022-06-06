'''
Системы счисления. Этап 1
    Напишите функции binary_to_decimal(bin_n) и decimal_to_binary(n) для перевода целых неотрицательных чисел из двоичной системы счисления в десятичную и наоборот. Функция binary_to_decimal(bin_n) принимает на вход строку, представляющую собой двоичную запись числа (например, "101101"), и возвращает целое число — значение в десятичной системе счисления. Функция decimal_to_binary(n) принимает на вход целое число n и возвращает строку, представляющую двоичную запись числа n. Кроме функций ничего писать не нужно.
'''


def binary_to_decimal(n):
    lst = list(map(lambda x, y: int(x) * 2 ** y, reversed(list(n)), range(0, len(n))))
    return sum(lst)


def decimal_to_binary(n):
    return "{0:b}".format(n)


print(decimal_to_binary(10))
print(binary_to_decimal("10111"))
