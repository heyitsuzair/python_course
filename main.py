class Employee:
    companyName = 'Apple'

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02

    def show_details(self):
        print(
            f"Name Of Employee Is {self.name} And The Raise Amount In {self.companyName} Is {self.raise_amount}")


emp = Employee('Uzair')
emp.raise_amount = 0.3
emp.companyName = 'Apple Pak'
emp.show_details()
Employee.companyName = 'Samsung'
# Employee.show_details(emp)
emp1 = Employee('Ahmed')
emp1.companyName ='Nestle'
emp1.show_details()
print(Employee.companyName)
