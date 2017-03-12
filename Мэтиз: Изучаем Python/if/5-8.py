"""
Hello Admin: создайте список из пяти и более имен пользователей, включающий имя
‘admin’. Представьте, что вы пишете код, который выводит приветственное сообщение для
каждого пользователя после его входа на сайт. Переберите элементы списка и выведите
сообщение для каждого пользователя.
•	 Для пользователя с именем 'admin’ выведите особое сообщение — например: «Hello
admin, would you like to see a status report?»
•	 В остальных случаях выводите универсальное приветствие — например: «Hello Eric,
thank you for logging in again»
"""

man = ["admin", "john", "mikki", "pol", "stiv"]

for m in man:
    if m == "admin":
        print("Hello", m, "would you like to see a status report?»")
    else:
        print("Hello", m, ",thank you for logging in again")
