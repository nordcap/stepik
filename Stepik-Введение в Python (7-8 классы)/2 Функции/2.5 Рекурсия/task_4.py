'''
Степень двойки
    Напишите рекурсивную функцию is_power(n), которая возвращает True, если переданное натуральное число является степенью двойки, и False иначе. Кроме функции ничего писать не нужно.
'''


def is_power2(n):
    if n == 1:
        return True
    else:
        return n % 2 == 0 and is_power(n / 2)


def is_power(n):
    return True if n == 1 else n % 2 == 0 and is_power(n / 2)


print(is_power(1048576))
