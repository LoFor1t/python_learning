from _9_12_users import User


class Privileges:
    def __init__(self):
        self.privileges = ['Allowed to add messages', 'Allowed to delete users', 'Allowed to ban users']

    def show_privileges(self):
        for privilege in self.privileges:
            if privilege == self.privileges[-1]:
                print(privilege + '.')
            else:
                print(privilege + ',')


class Admin(User):
    def __init__(self, first_name, last_name, age, nationality):
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = Privileges()