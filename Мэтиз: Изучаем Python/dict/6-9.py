"""
Любимые места: создайте словарь с именем favorite_places. Придумайте названия трех
мест, которые станут ключами словаря, и  сохраните для каждого человека от одного до
трех любимых мест. Чтобы задача стала более интересной, опросите нескольких друзей
и соберите реальные данные для своей программы. Переберите данные в словаре, выведи-
те имя каждого человека и его любимые места.
"""
favorite_places = {
    "london": ['Piter pan', 'jeck potroshitel', 'john tolkin'],
    "paris": ['john tolkin', 'sedric diggori'],
    "minsk": ['lukashenko', 'jeck potroshitel']
}
man = []
for mans in favorite_places.values():
    for m in mans:
        man.append(m)

for m in set(man):
    fav_place = []
    for place, people in favorite_places.items():
        if m in people:
            fav_place.append(place)
    print(m.title(), 'love', " and ".join(fav_place))
