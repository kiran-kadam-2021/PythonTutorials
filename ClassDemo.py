class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is ', self.cpu, self.ram)
        # print(type(self))


comp1 = Computer('i5', 8)
comp2 = Computer('i3', 16)
# Computer.config(comp1)
comp1.config()
comp2.config()
# print(type(comp1))

