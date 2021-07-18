class A:
    def __init__(self):
        print('in init of A')

    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')


# inheritance in python
# class B(A):
#     def __init__(self):
#         # super().__init__()
#         print('in init of B')
#
#     def feature3(self):
#         print('feature3 is working')
#
#     def feature4(self):
#         print('feature4 is working')


# b1 = B()

class B:
    def __init__(self):
        print('in init of B')

    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('feature4 is working')


class C(A, B):

    def __init__(self):
        super().__init__()
        print('in init of C')

    def feature5(self):
        print('feature5 is working')


c1 = C()
