'''
Делители 2
Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.
'''


def get_factors(num):
    arr = []
    for i in range(1, num + 1):
        if num % i == 0:
            arr.append(i)
    return arr


# объявление функции
def number_of_factors(num):
    return len(get_factors(num))


print(number_of_factors(1))
print(number_of_factors(5))
print(number_of_factors(10))
