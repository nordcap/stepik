'''
Подвиг 8. Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать их в список lst , затем, удалить последнее значение и если оно нечетное, то в список (в конец) добавить True, иначе - False. Отобразить полученный список на экране командой:

print(*lst)

Реализовать программу без использования условного оператора.
'''

lst = list(map(int, input().split()))
last = lst.pop()
lst.append(last % 2 != 0)
print(*lst)
