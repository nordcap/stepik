"""
Администратор: администратор — особая разновидность пользователя. Напишите
класс с  именем Admin, наследующий от класса User из упражнения 9-3 (с.  165) или
упражнения 9-5 (с. 170). Добавьте атрибут privileges для хранения списка строк вида
«разрешено добавлять сообщения», «разрешено удалять пользователей», «разрешено
банить пользователей» и  т.  д. Напишите метод show_privileges() для вывода набора
привилегий администратора. Создайте экземпляр Admin и вызовите свой метод.
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
    def __init__(self, first_name, last_name, login, email, privileges):
        super(Admin, self).__init__(first_name, last_name, login, email)
        self.privileges = privileges

    def show_privileges(self):
        for i, v in enumerate(self.privileges):
            print(i+1, '-', v)


adm = Admin('Ivan', 'Ivanov', 'admin', 'admin@mail.ru',
            ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей'])
print('Привилегии', end=":  ")
adm.describe_user()
adm.show_privileges()
