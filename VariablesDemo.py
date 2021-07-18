class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.comp = 'BMW'

    @staticmethod
    def say():
        print('hello')


c1 = Car()
c2 = Car()
c1.mil = 5
c2.comp = 'mercedes'
c1.wheels = 7
print(Car.say())
print(c1.comp, c1.mil, c1.wheels)
print(c2.comp, c2.mil, c2.wheels)
