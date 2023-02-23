class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_str(cls, string):
        return cls(string.split('-')[0], int(string.split('-')[1]))

# e = Employee('Uzair', 10000)
# print(e.name)
# print(e.salary)


string = 'Uzair-12000'
e = Employee.from_str(string)
print(e.name)
print(e.salary)
