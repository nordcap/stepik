'''
Подвиг 7. Объявите функцию с двумя параметрами width и height (ширина и высота прямоугольника), которая выводит сообщение (без кавычек):

"Периметр прямоугольника, равен x"

где x - вычисленный периметр прямоугольника. После объявления функции прочитайте (с помощью функции input) два целых числа, записанных в одну строку через пробел, и вызовите функцию с этими значениями.
'''


def myfunc(width, height):
    print(f"Периметр прямоугольника, равен {2 * (width + height)}")


lst = list(map(int, input().split()))
myfunc(lst[0], lst[1])
