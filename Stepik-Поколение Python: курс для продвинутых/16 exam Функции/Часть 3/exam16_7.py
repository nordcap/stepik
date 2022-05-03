'''
Напишите функцию compose(), которая принимает на вход две других одноаргументных функции f и g и возвращает новую функцию. Эта новая функция также должна принимать один аргумент x и применять к нему исходные функции в нужном порядке: для функций f и g порядок применения должен выглядеть, как f(g(x)).
'''

def compose(f, g):
    def res_compose(x):
        return f(g(x))
    return res_compose



def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))