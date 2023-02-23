class Employee:
    name = 'Uzair'

    def __len__(self):

        i = 0
        for c in self.name:
            i += 1
        return i

    def __str__(self):
        return f"Name Of Employee Is {self.name} str"

    def __repr__(self):
        return f"Name is Of Employee Is {self.name} repr"

    def __call__(self):
        print('Hey I am good')
