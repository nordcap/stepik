'''
Делители 1
Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа.
'''


# объявление функции
def get_factors(num):
    arr = []
    for i in range(1, num + 1):
        if num % i == 0:
            arr.append(i)
    return arr


print(get_factors(1))
print(get_factors(5))
print(get_factors(10))
