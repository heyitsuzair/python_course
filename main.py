class Employee:
    def __init__(self):
        self.__name = 'Uzair'  # "__" for private

    def greet(self):
        print(f"Hey {self.__name}")


a = Employee()
a.greet()
print(a._Employee__name)
