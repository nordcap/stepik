"""
Без пользователей: добавьте в hello_admin.py команду if, которая проверит, что список
пользователей не пуст.
•	 Если список пуст, выведите сообщение: «We need to find some users!»
•	 Удалите из списка все имена пользователей и убедитесь в том, что программа выво-
дит правильное сообщение.
"""

man = []
if man:
    for m in man:
        if m == "admin":
            print("Hello", m, "would you like to see a status report?»")
        else:
            print("Hello", m, ",thank you for logging in again")
else:
    print("We need to find some users!»")
