'''
Подвиг 6. Имеется вложенный список из трех строк:

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
Необходимо реализовать проверку на наличие в этом списке введенного слова. Результат (True или False) вывести на экран. Решить задачу необходимо без применения условного оператора.
'''

t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]

w = input()
print((w in t[0]) or (w in t[1]) or (w in t[2]))
