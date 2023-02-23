# class Parent:
#     def parent_method(self):
#         print('This Is Parent Method')


# class Child(Parent):
#     def parent_method(self):
#         print('This Is parent Method')
#         super().parent_method()

#     def child_method(self):
#         print('This Is Child Method')
#         super().parent_method()


# child_object = Child()
# child_object.child_method()
# child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Programmer(Employee):
    def __init__(self, name, id, lang):
        self.lang = lang
        super().__init__(name,id)


a = Employee('Uzair', "420")
b = Programmer('Ahmed', '202', 'Python')
print(b.name)
print(b.id)
print(b.lang)
