class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"Name Of Employee Is {self.name} And ID Is {self.id}")

class Programmer(Employee):
    def show_lang(self):
        print(f"Default Language Is Python")

emp = Employee('Uzair', 402)
emp.show_details()

emp2=Programmer('Ahmed',101)
emp2.show_lang()