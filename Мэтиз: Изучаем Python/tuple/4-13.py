"""
4-13. Шведский стол: меню «шведского стола» в ресторане состоит всего из пяти пунктов.
Придумайте пять простых блюд и сохраните их в кортеже.
•	 Используйте цикл for для вывода всех блюд, предлагаемых рестораном.
•	 Попробуйте изменить один из элементов и убедитесь в том, что Python отказывается
вносить изменения.
•	 Ресторан изменяет меню, заменяя два элемента другими блюдами. Добавьте блок
кода, который заменяет кортеж, и используйте цикл for для вывода каждого элемента
обновленного меню.
"""

food = ("суп", "чай", "салат", "сок", "котлета с картофелем")
print("-----------Старое меню----------")
for i in food:
    print(i)
#food[0] = "грибы"
new_food = ("суп", "кофе", "макароны", "сок", "котлета с картофелем")
print("-----------Новое меню----------")
for i in new_food:
    print(i)
