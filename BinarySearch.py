pos = -1


def search(lst, n):
    low, high = 0, len(lst)-1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == n:
            globals()["pos"] = mid
            return True
        elif lst[mid] < n:
            low = mid + 1
        else:
            high = mid - 1

    return False


lst = [1, 3, 9, 13, 17, 60, 64, 98, 110]
n = 64

if search(lst, n):
    print('Found at index', pos)
else:
    print('Not Found')
