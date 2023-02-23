class Math:

    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        print(a+b)


a = Math(11)
print(a.num)
a.add_to_num(6)
print(a.num)
Math.add(1,2)