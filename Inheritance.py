class A:
    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')


# inheritance in python
class B(A):
    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('feature4 is working')


# we can have multiple inheritance as well simultaneously
class C(B):
    def feature5(self):
        print('feature 5')


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature3()
b1.feature4()
b1.feature1()

c1 = C()
c1.feature1()
