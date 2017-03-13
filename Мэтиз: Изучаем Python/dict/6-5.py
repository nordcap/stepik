"""
6-5. Реки: создайте словарь с тремя большими реками и странами, по которым протекает
каждая река. Одна из возможных пар «ключ—значение» — ‘nile’: ‘egypt’.
•	 Используйте цикл для вывода сообщения с упоминанием реки и страны — например,
«The Nile runs through Egypt.»
•	 Используйте цикл для вывода названия каждой реки, включенной в словарь.
•	 Используйте цикл для вывода названия каждой страны, включенной в словарь.
"""
rivers = {
    'nile': 'egypt',
    'enisey': 'russia',
    'gang': 'india'
}
for i, v in rivers.items():
    print("The " + i + " runs through " + v + ".")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
