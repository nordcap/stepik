'''
Is a Number Prime? 🌶️
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True если число является простым и False в противном случае.
'''


# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num + 1):
        if num % i != 0:
            continue
        elif num % i == 0 and num != i:
            return False
    return True


print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
