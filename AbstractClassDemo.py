# to make any class abstract we need to
# import ABC=> Abstract Base Class and abstract method
# from abc
from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    def execute(self):
        print('executing...')


class Laptop(Computer):
    def process(self):
        print('running...')


# comp = Computer()
c1 = Laptop()
c1.process()
c1.execute()
