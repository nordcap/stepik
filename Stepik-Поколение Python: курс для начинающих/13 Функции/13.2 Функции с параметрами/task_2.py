'''
ФИО
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.

Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.
'''


# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0].capitalize() + name[0].capitalize() + patronymic[0].capitalize())


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
