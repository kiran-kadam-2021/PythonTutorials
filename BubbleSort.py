def sort(lst):
    i, j, n = 0, 0, len(lst)
    while i < n-1:
        j = 0
        while j < n-i-1:
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            j += 1
        i += 1


lst = [9, 34, 11, 10, 92, 156, 35, 314, 2587, 3, 2, 461]
sort(lst)
print(lst)
