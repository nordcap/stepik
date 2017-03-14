"""
Великие фокусники: начните с копии вашей программы из упражнения 8-9. Напишите
функцию make_great(), которая изменяет список фокусников, добавляя к  имени каждого
фокусника приставку «Great». Вызовите функцию show_magicians() и убедитесь в том, что
список был успешно изменен.
"""


def show_magicians(lst_name):
    for i in lst_name:
        print(i)


def make_great(lst_name):
    for i, v in enumerate(lst_name):
        lst_name[i] = "Великий " + v


l = ['фокусник1', "фокусник2", "фокусник3"]
make_great(l)
show_magicians(l)
