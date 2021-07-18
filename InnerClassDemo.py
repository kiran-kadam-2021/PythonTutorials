class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lp = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lp.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('kiran', 2)
s2 = Student('dips', 3)
s1.show()
s2.show()
