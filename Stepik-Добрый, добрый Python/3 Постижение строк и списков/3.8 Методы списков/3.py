'''
Подвиг 4. Вводится строка с номером телефона в формате:

+7(xxx)xxx-xx-xx

Необходимо преобразовать ее в список lst (посимвольно, то есть, элементами списка будут являться отдельные символы строки). Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы. Отобразить полученный список на экране командой:

print("".join(lst))
'''

lst = list(input())

lst.pop(0)
lst[0] = '8'
lst.remove('-')
lst.remove('-')
print("".join(lst))
