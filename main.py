class Person:
    def __init__(self,name,country,age):
        self.name=name
        self.country=country
        self.age=age

    def info(self):
        print(f"{self.name} is {self.age} years old and he lives in {self.country}")


a = Person('Uzair','Pakistan',10)
b = Person('Ahmed','UK',5)
c = Person(country='USA',age=20,name='Ali')
a.info()
b.info()
c.info()
