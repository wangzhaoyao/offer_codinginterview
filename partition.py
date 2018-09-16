def partition(alist, start, end):
    if end <= start:
        return
    base = alist[start]
    index1, index2 = start, end
    while start < end:
        while start < end and alist[end] >= base:
            end -= 1
        alist[start] = alist[end]
        while start < end and alist[start] <= base:
            start += 1
        alist[end] = alist[start]
    alist[start] = base
    partition(alist, index1, start - 1)
    partition(alist, start + 1, index2)

def find_least_k_nums(alist, k):
    length = len(alist)
    if not alist or k <=0 or k > length:
        return None
    start = 0
    end = length - 1
    partition(alist, start, end)
    return alist[:k]
if __name__ == "__main__":
    l = [1, 9, 2, 4, 7, 6, 3,10,4,5]
    min_k = find_least_k_nums(l, 4)
    print (min_k)