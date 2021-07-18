# def add_sub(x, y):
#     return x+y, x-y
#
#
# a, b = add_sub(9, 366)
# print(a, b)

# def update(x=5):  # default value
#     print(id(x))
#     x[1] += 1
#     print(id(x))
#     print(x)
#
#
# a = [10, 39, 64]
# print(id(a))
# update(a)  # by default we pass shallow copy to pass deep copy should mention a.copy()
# print(a)


# def update(x=5):
#     x += 1
#     print(x)
#
#
# update()  # call default valued argumented function
# update(x=67)  # calls keyworded argumented function


# def add(*arr):  # variable number of arguments
#     n = 0
#     for i in arr:
#         n += i
#     return n
#
#
# print(add(3, 4, 6))

# def person(name, **data):  # keyworded variable length arguments
#     for i, j in data.items():
#         print(i, j)
#
#
# person('navin', age=24, city='Mumbai', mob=365412)


# a = 10
#
#
# def something():
#     a = 9
#     print(a)
#     globals()['a'] = 100
#     a = 15
#     print(a)
#
#
# something()
# print(a)

# example
# def count_names(lst):
#     count = 0
#
#     for name in lst:
#         if len(name) >= 5:
#             count += 1
#
#     return count
#
#
# lst = ['kirahj', 'jxhjalkjx', 'jxkjhs', ' k', 'knasskhi', 'ku']
# print(count_names(lst))

