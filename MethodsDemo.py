class Student:

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance methods
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    # class methods
    @classmethod
    def get_school(cls):
        return cls.school

    # static methods
    @staticmethod
    def info():
        print('This is student class in the module')


s1 = Student(64, 35, 67)
s2 = Student(65, 38, 94)

print(s1.avg())
print(Student.get_school())
