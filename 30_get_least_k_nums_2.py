import heapq
def get_least_numbers_big_data(alist, k):
    max_heap = []
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return
    k = k - 1
    for ele in alist:
        ele = -ele
        if len(max_heap) <= k:
            heapq.heappush(max_heap, ele)
        else:
            heapq.heappushpop(max_heap, ele)

    return map(lambda x:-x, max_heap)


if __name__ == "__main__":
    l = [1,1, 9, 2, 4, 7, 6, 3]
    min_k = get_least_numbers_big_data(l, 3)
    res=[]
    for i in min_k:
        res.append(i)
    print(res)