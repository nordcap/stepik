"""
Попытки входа: добавьте атрибут login_attempts в  класс User из упражнения 9-3
(с.  165). Напишите метод increment_login_attempts(), увеличивающий значение login_
attempts на 1. Напишите другой метод с именем reset_login_attempts(), обнуляющий значе-
ние login_attempts.
Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз. Вы-
ведите значение login_attempts, чтобы убедиться в том, что значение было изменено пра-
вильно, а  затем вызовите reset_login_attempts(). Снова выведите login_attempts и  убеди-
тесь в том, что значение обнулилось.
"""


class User():
    def __init__(self, first_name, last_name, login, email):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("info user:")
        print(self.first_name, self.last_name, "(" + self.login + ")", "email=", self.email)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Ivan", "Ivanov", "ivanok", "ivanov@mail.ru")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
