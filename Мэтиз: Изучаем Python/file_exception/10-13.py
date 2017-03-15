"""
10-13. Проверка пользователя: последняя версия remember_me.py предполагает, что поль-
зователь либо уже ввел свое имя, либо программа выполняется впервые. Ее нужно из-
менить на тот случай, если текущий пользователь не является тем человеком, который
последним использовал программу.
Прежде чем выводить приветствие в  greet_user(), спросите пользователя, правильно
ли определено имя пользователя. Если ответ будет отрицательным, вызовите get_new_
username() для получения правильного имени пользователя.
"""
import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        answer = input(username + "! Правильно ли определено имя пользователя? (y/n) ")
        if answer == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
