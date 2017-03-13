"""
Люди: начните с программы, написанной для упражнения 6-1 (с. 107). Создайте два
новых словаря, представляющих разных людей, и  сохраните все три словаря в  списке
с именем people . Переберите элементы списка людей. В процессе перебора выведите всю
имеющуюся информацию о каждом человеке.
"""
man_1 = {
    "first_name": "Dmitriy",
    "last_name": "Medvedev",
    "age": 50,
    "city": "Moskou"
}
man_2 = {
    "first_name": "Dmitriy",
    "last_name": "Rogozin",
    "age": 45,
    "city": "Moskou"
}
man_3 = {
    "first_name": "Dmitriy",
    "last_name": "Ivanov",
    "age": 60,
    "city": "Moskou"
}
people = [man_1, man_2, man_3]
for man in people:
    for i, v in man.items():
        print(i, ":", v, end="; ")
    print()
