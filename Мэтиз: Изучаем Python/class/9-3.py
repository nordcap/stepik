"""
Пользователи: создайте класс с именем User. Создайте два атрибута first_name и last_
name, а  затем еще несколько атрибутов, которые обычно хранятся в  профиле пользова-
теля. Напишите метод describe_user(), который выводит сводку с информацией о пользо-
вателе. Создайте еще один метод greet_user() для вывода персонального приветствия для
пользователя.
Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба
метода для каждого пользователя.
"""


class User():
    def __init__(self, first_name, last_name, login, email):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.email = email

    def describe_user(self):
        print("info user:")
        print(self.first_name, self.last_name, "(" + self.login + ")", "email=", self.email)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())


user_1 = User("Ivan", "Ivanov", "ivanok", "ivanov@mail.ru")
user_2 = User("Petunya", "Petrov", "petko", "petrov@gmail.com")
user_3 = User("Andrey", "Amosov", "amo", "amosov@mail.ru")

user_1.describe_user()
user_1.greet_user()
print("------------------")
user_2.describe_user()
user_2.greet_user()
print("------------------")
user_3.describe_user()
user_3.greet_user()
