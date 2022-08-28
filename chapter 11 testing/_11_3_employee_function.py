class Employee:
    """Представляет информацию о работнике."""

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, new_salary=5000):
        self.salary += new_salary


