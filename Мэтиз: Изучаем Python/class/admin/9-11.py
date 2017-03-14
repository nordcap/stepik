"""
9-11. Импортирование класса Admin: начните с версии класса из упражнения 9-8 (с. 176).
Сохраните классы User, Privileges и Admin в одном модуле. Создайте отдельный файл, соз-
дайте экземпляр Admin и вызовите метод show_privileges(), чтобы показать, что все рабо-
тает правильно.
"""
from admin import Admin

adm = Admin('Ivan', 'Ivanov', 'admin@mail.ru', 'admin')
print('Привилегии', end=":  ")
adm.describe_user()
adm.privileges.show_privileges()
