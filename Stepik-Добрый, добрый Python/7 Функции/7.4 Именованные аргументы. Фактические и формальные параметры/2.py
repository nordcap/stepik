'''
Подвиг 3. Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль) и имеет один формальный параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять: есть ли в пароле хотя бы один символ из chars и что длина пароля не менее 8 символов. Если проверка проходит, то функция возвращает True, иначе - False.
'''


def check_password(passwd, chars='$%!?@#'):
    if len(passwd) < 8:
        return False
    for i in chars:
        if i in passwd:
            return True
    return False


print(check_password('12345678!'))
