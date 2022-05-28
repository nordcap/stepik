'''
Валидация пароля. Этап 1
        Список худших паролей почти не меняется из года в год, однако люди часто не придают большого значения безопасности в интернете. Один из ваших предыдущих клиентов хочет запустить валидацию пароля на своем сайте и попросил вас написать для него простенькую программу. Программа принимает на вход строку с паролем и выводит “Bad password”, если выполняется хотя бы одно из условий:

пароль содержит подстроку qwerty или подстроку 1234

пароль короче восьми символов

пароль не содержит ни одну цифру

и "Good password" иначе.
'''
import string

passwd = input()
if len(passwd) < 8 or 'qwerty' in passwd or '1234' in passwd or \
        (
                '0' not in passwd and '1' not in passwd and '2' not in passwd and '3' not in passwd and '4' not in passwd and '5' not in passwd and '6' not in passwd and '7' not in passwd and '8' not in passwd and '9' not in passwd):
    print("Bad password")
else:
    print("Good password")
