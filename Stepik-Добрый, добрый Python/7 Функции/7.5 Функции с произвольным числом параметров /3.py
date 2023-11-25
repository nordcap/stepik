'''

Подвиг 5. Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника. На вход этой функции передаются N длин сторон через аргументы. Дополнительно могут быть указаны именованные аргументы:

type - булево значение True/False
color - целое числовое значение
closed - булево значение True/False
width - целое значение

Функция должна возвращать в виде кортежа периметр многоугольника и указанные значения именованных параметров в порядке их перечисления в тексте задания (если они были переданы). Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).
'''


def get_data_fig(*args, **kwargs):
    res = (sum(args),)
    if 'type' in kwargs:
        res += (kwargs['type'],)
    if 'color' in kwargs:
        res += (kwargs['color'],)
    if 'closed' in kwargs:
        res += (kwargs['closed'],)
    if 'width' in kwargs:
        res += (kwargs['width'],)
    return res


print(get_data_fig(1, 2, 3, type=True, color=5, closed=False, width=2))
