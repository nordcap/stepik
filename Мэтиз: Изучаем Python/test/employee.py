"""
11-3. Работник: напишите класс Employee, представляющий работника. Метод __init__()
должен получать имя, фамилию и ежегодный оклад; все эти значения должны сохраняться
в атрибутах. Напишите метод give_raise(), который по умолчанию увеличивает ежегодный
оклад на $5000 — но при этом может получать другую величину прибавки.
Напишите тестовый сценарий для Employee. Напишите два тестовых метода, test_give_
default_raise() и  test_give_custom_raise(). Используйте метод setUp(), чтобы вам не при-
ходилось заново создавать экземпляр Employee в каждом тестовом методе. Запустите свой
тестовый сценарий и убедитесь в том, что оба теста прошли успешно.
"""


class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add_salary=5000):
        self.salary += add_salary
