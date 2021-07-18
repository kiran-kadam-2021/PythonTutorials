# from math import *
#
#
# def fact(x):
#     ans = 1
#
#     if x < 0:
#         return
#     elif x == 0:
#         ans = 1
#         return ans
#
#     for i in range(1, x+1):
#         ans *= i
#
#     return ans
#
#
# print(fact(6))
# print(factorial(6))

# def fact(x):
#     if x == 0: return 1
#     else: return x * fact(x-1)
#
#
# print(fact(7))

# import sys
# print(sys.getrecursionlimit())

# f = lambda a, b: a + b
#
# res = f(6, 5)
# print(res)


# from functools import reduce
# nums = [3, 6, 9, 8, 0, 15, 67, 8, 6, 97, 37]
# evens = list(filter(lambda a: a % 2 == 0, nums))
# odds = list(filter(lambda a: a % 2 == 1, nums))
# print(evens)
# print(odds)

# doubles = list(map(lambda a: a*2, evens))
# print(doubles)

# sum1 = reduce(lambda a, b: a+b, evens)
# print(sum1)


