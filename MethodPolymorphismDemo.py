class A:
    def show(self):
        print('in A show')


class B(A):
    # pass
    def show(self):
        print('in B show')


b1 = B()
b1.show()
