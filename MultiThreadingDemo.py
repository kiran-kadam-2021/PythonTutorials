from threading import *
from time import sleep


class Hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)


class Hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)


t1 = Hi()
t2 = Hello()

t1.start()
sleep(0.2)  # sleep time is in seconds
t2.start()

# join() will wait for t1 t2 thread
# to complete its execution
t1.join()
t2.join()

print('bye')
