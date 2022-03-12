'''
BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка и False в противном случае.
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
def is_valid_password(password):
    arr_passwd = [i for i in password.split(':')]
    if len(arr_passwd) == 3:
        if arr_passwd[0] == arr_passwd[0][::-1] and is_prime(int(arr_passwd[1])) and int(arr_passwd[2]) % 2 == 0:
            return True

    return False


print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
