class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        return Student(self.m1+other.m1, self.m2+other.m2)

    def show(self):
        print(self.m1, self.m2)

    def __gt__(self, other):
        if self.m1 < other.m1:
            return False
        elif self.m1 == other.m1 and self.m2 < other.m2:
            return False

        return True

    def __str__(self):
        # return str(self.m1) + ' ' + str(self.m2)
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(58, 72)
s2 = Student(60, 62)

# + is overloaded here
# when used + internally __add__() is called
# s3 = s1 + s2 => s3 = s1.__add__(s2)
s3 = s1 + s2
# s1.show()
# s2.show()
# s3.show()

if s2 > s1:  # here '>' is overloaded
    print('s2 is greater than s1')

# when we print an integer x then x.__str__() is called
# so we will override __str__() in student to show Student
print(s1)
print(s2)
print(s3)
