"""
Пользовательские альбомы: начните с программы из упражнения 8-7. Напишите цикл
while, в котором пользователь вводит исполнителя и название альбома. Затем в цикле вы-
зывается функция make_album() для введенных пользователей и  выводится созданный
словарь. Не забудьте предусмотреть признак завершения в цикле while.
"""


def make_album(name, album, count=''):
    album_dict = {}
    if count:
        album_dict["count"] = count
    album_dict["name_singer"] = name
    album_dict["name_album"] = album
    return album_dict


while True:
    singer = input("Введите исполнителя:")
    album = input("Введите альбом:")
    count = input("Введите количество дорожек:")
    a = make_album(singer, album, count)
    print(a)
    active = input("Закончить (yes)")
    if active == 'yes':
        break
