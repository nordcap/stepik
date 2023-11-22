'''
Подвиг 8. Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки. Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.

После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.
'''


def check_email(email):
    t = {'A', 'E', 'I', 'O', 'U', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
         'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y',
         'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@',
         '.'}
    flag = True

    for i in email:
        if i not in t:
            flag = False
            break

    if not flag:
        print("НЕТ")
        exit(0)

    if not (email[0].isalpha() and email[-1].isalpha()):
        print("НЕТ")
        exit(0)

    if email.count('@') > 1:
        print("НЕТ")
        exit(0)

    if email.count('.') > 0 and email.count('@') > 0:
        idx1 = email.index('@')
        idx2 = email.index('.')
        if not (idx2 > idx1):
            flag = False
    else:
        print("НЕТ")
        exit(0)

    if flag:
        print("ДА")
    else:
        print("НЕТ")


s = input().strip()

check_email(s)
