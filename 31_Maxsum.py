def function(lists):
    max_sum = lists[0]
    pre_sum = 0
    for i in lists:
        if pre_sum < 0:
            pre_sum = i
        else:
            pre_sum += i
        if pre_sum > max_sum:
            max_sum = pre_sum
    return max_sum


def main():
    lists = [-6, -4,-3, -1, -2, -7, -3,-9,-15, -1, -2, -2]
    print (function(lists))


if __name__ == "__main__":
    main()