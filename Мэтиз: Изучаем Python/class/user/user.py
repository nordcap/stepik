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
