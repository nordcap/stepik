'''
Подвиг 2. Вводится строка с номером телефона. Ожидается формат ввода:

+7(xxx)xxx-xx-xx

где x - это цифра. Размер введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя). Необходимо проверить, что введенная строка соответствует этому формату. Вывести ДА, если соответствует и НЕТ - в противном случае.
'''

telephone = input()
flag = True
for i, d in enumerate(telephone):
    if telephone[0] != '+' or telephone[1] != '7' or telephone[2] != '(' or telephone[6] != ')':
        flag = False
        break
    if i in [3, 4, 5, 7, 8, 9, 11, 12, 14, 15] and not d.isdigit():
        flag = False
        break
    if i in [10, 13] and d != '-':
        flag = False
        break

if flag:
    print('ДА')
else:
    print('НЕТ')
