def search(list, n):

    i = 0
    while i < len(list):
        if list[i] == n:
            return i
        i += 1

    return -1


list = [2, 9, 3, 6, 5, 7]

n = 7
index = search(list, n)

if index != -1:
    print('Found at index', index)
else:
    print('Not found')
