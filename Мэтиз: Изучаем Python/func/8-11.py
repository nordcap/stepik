"""
8-11. Фокусники без изменений: начните с программы из упражнения 8-10. Вызовите функ-
цию make_great() и  передайте ей копию списка имен фокусников. Поскольку исходный
список остался неизменным, верните новый список и  сохраните его в  отдельном списке.
Вызовите функцию show_magicians() с каждым списком, чтобы показать, что в одном спи-
ске остались исходные имена, а в другом к имени каждого фокусника добавилась приставка
«Great».
"""


def show_magicians(lst_name):
    for i in lst_name:
        print(i)


def make_great(lst_name):
    for i, v in enumerate(lst_name):
        lst_name[i] = "Великий " + v
    return lst_name


mag = ['фокусник1', "фокусник2", "фокусник3"]
great_mag = make_great(mag[:])
show_magicians(mag)
show_magicians(great_mag)
