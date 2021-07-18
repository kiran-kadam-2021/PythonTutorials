class Computer:
    def __init__(self):
        self.name = 'kk'
        self.age = 12

    def update(self):
        self.age = 25

    def compare(self, obj):
        return self.age == obj.age


c1 = Computer()
c2 = Computer()
c1.name = 'kiran'
print(id(c1.name))
print(id(c2.name))

# c1.update()
# print(c1.age)
# print(c2.age)

if c1.compare(c2):
    print('They are same')
else:
    print('They are not')

