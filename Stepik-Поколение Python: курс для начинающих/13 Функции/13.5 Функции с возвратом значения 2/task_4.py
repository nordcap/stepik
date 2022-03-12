'''
Good password 🌶️
Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:

его длина не менее 88 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
'''


# объявление функции
def is_password_good(password):
    arr_upper = [i for i in password if i.isupper() == True]
    arr_lower = [i for i in password if i.islower() == True]
    arr_digit = [i for i in password if i.isdigit() == True]

    if len(password) >= 8 and len(arr_upper) >= 1 and len(arr_lower) >= 1 and len(arr_digit) >= 1:
        return True
    else:
        return False


print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))
