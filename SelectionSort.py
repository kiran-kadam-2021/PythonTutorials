def sort(lst):
    n = len(lst)
    for i in range(n-1):
        index = i
        j = i+1
        while j < n:
            if lst[index] > lst[j]:
                index = j
            j += 1
        lst[i], lst[index] = lst[index], lst[i]
        print(lst)


lst = [9, 34, 11, 10, 92, 156, 35, 314, 2587, 3, 2, 461]
sort(lst)
print(lst)
