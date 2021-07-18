# # reading file and printing it to console
# f = open('MyFile', 'r')
# # reads current line pointed by 'f'
# print(f.readline())
#
# # reads 2 characters of current line
# print(f.readline(2))
#
# # # returns list of all lines after the current line
# # print(f.readlines())
#
# # from the list reads a specified line
# print(f.readlines()[0])
#
# f.close()

# # writing to a file
# f = open('MyFile', 'a')
#
# f.write('kiran\n')
# f.write('kadam\n')
# f.write('kk\n')
#
# f.close()


# # copying one text file to another
# f1 = open('MyFile', 'r')
# f2 = open('MyData', 'a')
#
# for data in f1:
#     f2.write(data)
#
# f1.close()
# f2.close()


# # copying image using code
# f1 = open('wallpaper.jfif', 'rb')
# f2 = open('MyImage.jfif', 'wb')
#
# for data in f1:
#     f2.write(data)
#
# f1.close()
# f2.close()
