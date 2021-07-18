# lst = [5, 8, 7]
#
# # for i in lst:
# #     print(i)
#
# it = iter(lst)
#
# print(it.__next__())
# print(it.__next__())
# print(next(it))

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()

it = iter(values)
print(it.__next__())
print(it.__next__())
print(next(it))

for i in values:  # i will start from 4
    print(i)
