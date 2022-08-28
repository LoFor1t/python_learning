class User:
    def __init__(self, first_name, last_name, age, nationality):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first.title()} {self.last.title()} is {self.age} years old, and has {self.nationality} "
              f"nationality.")

    def greet_user(self):
        print(f"Hello, {self.first.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0