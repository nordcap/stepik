'''
Bookflix
    Напишите рекомендательную систему для нового сервиса Bookflix, подбирающего книги для пользователя. Сервис хранит все прочитанные пользователем книги и по его запросу "Посоветуй мне книгу" должен подобрать набор книг, соответствующий критериям:

книга не должна быть прочитана пользователем ранее.

книга должна быть в любимом жанре пользователя. Любимый жанр – это жанр, который чаще всего встречается в списке прочитанных книг. Любимых жанров может быть несколько.

    Формат ввода: первая строка – список всех книг сервиса, передающихся через запятую. В описание книги входит фамилия автора, название в кавычках и жанр в скобках. Каждая последующая строка описывает одно из двух действий: уведомление о прочтении книги или запрос совета. Когда пользователь прочитывает книгу, программа через пробел принимает имя пользователя и название книги. Когда пользователь просит совета, программа принимает строку "Посоветуй мне книгу" и имя пользователя в скобках. Ввод строк заканчивается точкой.

    Формат вывода: после каждой просьбы совета необходимо вывести список книг через запятую, названия книг указываются в кавычках. Если нельзя рекомендовать ни одну книгу, выведите "Список пуст". Порядок книг в списке не важен.

    Гарантируется, что пользователи читают только книги из списка, а также то, что названия книг разных авторов не совпадают.
'''


def is_janre(lib, book):
    # определение к какому жанру относится книга
    for key, val in lib.items():
        if book in val:
            return key


def love_janre(user, dict_user):
    # поиск любимого жанра
    lst_love_janre = []

    max_count = 0
    for arr in dict_user[user].values():
        if max_count < len(arr):
            max_count = len(arr)
    # вернуть все жанры с наибольшим кол-вом прочитанных книг
    for janre, arr_books in dict_user[user].items():
        if max_count == len(arr_books):
            lst_love_janre.append(janre)
    return lst_love_janre


def union_books_janre(arr_love_janre, lib):
    # объединение книг из любимых жанров
    arr_result = []
    for janre in arr_love_janre:
        arr_result = arr_result + lib[janre]
    return arr_result


def offer_me(arr_union_books, dict_user_read):
    # выдача предложения по условию - книга не должна прочитана ранее
    arr_read = parse_list(list(dict_user_read.values()))
    arr_result = []
    for book in arr_union_books:
        if book in arr_read:
            continue
        else:
            arr_result.append(book)

    return arr_result


def parse_list(input_array):
    # конвертация вложенных списков в односвязный
    result_array = []
    for array_item in input_array:
        if isinstance(array_item, list) or isinstance(array_item, tuple):
            result_array.extend(parse_list(array_item))
        else:
            result_array.append(array_item)
    return result_array


#################################################################################
##################################################################################################################################################################
list_books = [book.strip() for book in input().split(',')]

'''
{
	сатира: ["Собачье сердце"],
	научная фантастика:["Марсианин", "Отравленный пояс" ]
}
'''
lib = dict()  # библиотека с жанрами

''' {Dontsova:{
(ужасы):["Оно", "Сияние"],
(фэнтези):["Властелин колец","Хоббит"]`
 }}
 '''
dict_user = dict()

for item in list_books:
    ind_1 = item.find('"')  # начало названия книги
    ind_2 = item.rfind('"')  # конец названия книги
    ind_3 = item.find('(')  # начало названия жанра

    janre = item[ind_3:]
    name_book = item[ind_1:ind_2 + 1]

    if janre not in lib:
        lib[janre] = []

    lib[janre].append(name_book)

while True:
    s = input()
    if s == '.':
        break
    if s.find("Посоветуй мне книгу") != -1:
        ind_1 = s.find("(")
        user = s[ind_1 + 1:-1]
        if user in dict_user:
            arr_love_janre = love_janre(user, dict_user)
            arr_union_books = union_books_janre(arr_love_janre, lib)
            offer = offer_me(arr_union_books, dict_user[user])
            if len(offer) > 0:
                print(*offer, sep=", ")
            else:
                print("Список пуст")
        else:
            print("Список пуст")

    else:
        # запись данных в словарь
        ind_1 = s.find(" ")
        user = s[0:ind_1]
        book = s[ind_1 + 1:]
        # находим жанр книги
        janre = is_janre(lib, book)

        if user not in dict_user:
            dict_user[user] = dict()

        if janre not in dict_user[user]:
            dict_user[user][janre] = []

        dict_user[user][janre].append(book)
