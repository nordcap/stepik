'''
Подвиг 6. Функции из предыдущего подвига 5 добавьте еще один формальный параметр up с начальным булевым значением True. Если параметр up равен True, то тег (указанный в формальном параметре tag) следует записывать заглавными буквами, а иначе - малыми.

После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию (с выводом результата ее работы на экран):

- первый раз со строкой и именованным аргументом tag со значением 'div'
- второй раз со строкой, именованным аргументом tag со значением 'div' и именованным аргументом up со значением False.
'''


def to_tag(str, tag='h1', up=True):
    tag = tag.upper() if up else tag.lower()
    return f"<{tag}>{str}</{tag}>"


input_str = input()
print(to_tag(input_str, tag='div'))
print(to_tag(input_str, tag='div', up=False))
