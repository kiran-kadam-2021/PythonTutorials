# # import sys
# # x = sys.argv[1]
# # z = pow(int(x), 3)
#
# x = int(input())
# z = pow(x, 3)
#
# print(z)

# x = int(input())
# z = x % 3
#
# if z == 0:
#     print('zero')
# elif z == 1:
#     print('one')
# elif z == 2:
#     print('two')
# print('Bye')


# i = 1
# while i < 5:
#     j = 1
#     while j <= 4:
#         print('# ', end="")
#         j += 1
#
#     i += 1
#     print()

# items = ['kiran', 'has', 'a', 'bike']
#
# for item in range(10, 0, -1):
#     if item % 5 != 0:
#         print(item, end=" ")

# x = int(input('how many candies u want : '))
# available = 10
# i = 1
# while i <= x:
#
#     if i > available:
#         break
#     print('candy')
#     i += 1
#
# print('Bye')

#

# for i in range(4):
#
#     for j in range(4-i):
#         print('#', end=" ")
#
#     print()


# for i in range(5):
#     print(i)

# from math import sqrt
# num = int(input())
#
# for i in range(2, int(sqrt(num))+1):
#     if num % i == 0:
#         print('not prime')
#         break
#
# else:
#     print('prime')

# from array import *
#
# values = array('i', [5, -9, 8, 3, 6, 10, 0])
# print(values)
# values.reverse()
# print(values)

# values.append(64)
# print(values)

# for i in values:
#     print(i)

# newArr = array(values.typecode, (a**2 for a in values))
# print(newArr)
#
# i = 0
# while i < len(newArr):
#     print(newArr[i], end=" ")
#     i += 1


# from array import *
#
# arr = array('i', [])
#
# n = int(input("Enter the length of array : "))
#
# for i in range(n):
#     x = int(input())
#     arr.append(x)
#
#
# val = int(input('Enter number to be find '))
# k = 0
# for e in arr:
#     if e == val:
#         print(k)
#         break
#
#     k += 1

# print(arr.index(val))

# from numpy import *
# arr = array([13, 68, 95, 67])
# print(sort(arr))
# print(arr)
# print(arr.dtype)

# from numpy import *
# arr = linspace(1, 100, 10)  # make 4 equal parts starting from 1 and ending on 100 with difference (100 -1)/ (10-1)
# arr = arange(1, 14, 2)  # starting from 1 and with diff = 2 all element les than equal to 14
# arr = zeros(5)  # create array of size 5 initialised it to 0
# arr = ones(5)  # create array of size 5 initialised it to 1
# arr = ones(5, int)
# print(arr)
# print(arr.dtype)

# from numpy import *
# arr = array([1, 5, 159, 67, 67, 5])
# arr1 = array([3, 9, 6, 7, 6, 1])
# arr += arr1  # vectorised operations
# print(arr)
# print(concatenate(arr, arr1))

# print(arr)
# print(unique(arr))

# from numpy import *
#
# arr = array([1, 5, 9, 6, 3])

# arr1 = arr.view()  # shallow copy - change in any array cause change in other also
# arr1 = arr.copy()  # deep copy - completely different array
# arr[1] = 100
# print(arr)
# print(arr1)
# print(id(arr))
# print(id(arr1))


# from numpy import *
#
# arr1 = array([
#     [1, 2, 3],
#     [9, 8, 7],
#     [15, 67, 94],
#     [37, 61, 28]
# ])

# print(arr1)
# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)


# arr2 = arr1.flatten()
# print(arr2)

# arr3 = arr2.reshape(2, 2, 3)
# print(arr3)

# m = matrix('1 2 3 ; 9 8 7; 15 67 94; 37 61 28')
# m = matrix(arr1)
# print(m)

# from numpy import *
#
# m = matrix('1 2 3; 4 15 6; 7 8 9')
# print(m)
# print(diagonal(m))
# print(m.max())
# m1 = matrix('0 1 1; 0 0 0; 1 0 0')
# m2 = m * m1
# print(m2)


