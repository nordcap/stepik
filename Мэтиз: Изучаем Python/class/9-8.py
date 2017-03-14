"""
Привилегии: напишите класс Privileges. Класс должен содержать всего один атрибут
privileges со списком строк из упражнения 9-7. Переместите метод show_privileges() в этот
класс. Создайте экземпляр Privileges как атрибут класса Admin. Создайте новый экземпляр
Admin и используйте свой метод для вывода списка привилегий.
"""


class User():
    def __init__(self, first_name, last_name, login, email):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.email = email

    def describe_user(self):
        print(self.first_name, self.last_name, "(" + self.login + ")", "email=", self.email)

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())


class Admin(User):
    def __init__(self, first_name, last_name, login, email):
        super(Admin, self).__init__(first_name, last_name, login, email)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей',
                           'разрешено банить пользователей']

    def show_privileges(self):
        for i, v in enumerate(self.privileges):
            print(i + 1, '-', v)


adm = Admin('Ivan', 'Ivanov', 'admin', 'admin@mail.ru')
print('Привилегии', end=":  ")
adm.describe_user()
adm.privileges.show_privileges()
