"""
Человек: используйте словарь для сохранения информации об известном вам чело-
веке. Сохраните имя, фамилию, возраст и город, в котором живет этот человек. Словарь
должен содержать ключи с такими именами, как first_name, last_name, age и city. Выведите
каждый фрагмент информации, хранящийся в словаре.
"""
man = {
    "first_name": "Dmitriy",
    "last_name": "Medvedev",
    "age": 50,
    "city": "Moskou"
}
print(man["first_name"])
print(man["last_name"])
print(man["age"])
print(man["city"])
