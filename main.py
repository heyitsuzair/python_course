class Person:
    name = 'Uzair'
    age = 20
    country = 'Pak'

    def info(self):
        print(f"{self.name} is {self.age} years old and he lives in {self.country}")


a = Person()
a.name = 'Ahmed'
a.age = 10
a.info()

b = Person()
b.name = 'Uzair'
b.age = 12
b.info()
