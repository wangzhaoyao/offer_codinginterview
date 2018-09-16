def partition(alist, start, end):
    if end <= start:
        return
    base = alist[start]
    # index1, index2 = start, end
    while start < end:
        while start < end and alist[end] >= base:
            end -= 1
        alist[start] = alist[end]
        while start < end and alist[start] <= base:
            start += 1
        alist[end] = alist[start]
    alist[start] = base
    return start


def find_least_k_nums(alist, k):
    length = len(alist)
    # if length == k:
    #    return alist
    if not alist or k <=0 or k > length:
        return
    start = 0
    end = length - 1
    index = partition(alist, start, end)
    while index != k:
        if index > k:
            index = partition(alist, start, index - 1)
        elif index < k:
            index = partition(alist, index + 1, end)
    return alist[:k]

if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3,10,5]
    min_k = find_least_k_nums(l, 6)
    print (min_k)


