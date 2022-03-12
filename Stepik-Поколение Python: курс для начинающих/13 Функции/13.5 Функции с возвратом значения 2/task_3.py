'''
Next Prime 🌶️🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
'''


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num + 1):
        if num % i != 0:
            continue
        elif num % i == 0 and num != i:
            return False
    return True


# объявление функции
def get_next_prime(num):
    flag = True
    while flag:
        num += 1
        if is_prime(num):
            flag = False
    return num


print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
