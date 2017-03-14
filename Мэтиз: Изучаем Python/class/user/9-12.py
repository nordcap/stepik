"""
9-12. Множественные модули: сохраните класс User в  одном модуле, а  классы Privileges
и Admin в другом модуле. В отдельном файле создайте экземпляр Admin и вызовите метод
show_privileges(), чтобы показать, что все работает правильно.
"""
from admin_privileges import Admin

adm = Admin('Ivan', 'Ivanov', 'admin@mail.ru', 'admin')
print('Привилегии', end=":  ")
adm.describe_user()
adm.privileges.show_privileges()
