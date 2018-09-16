# -*-coding：utf-8 -*-

def fabonacci(n):
    a1, a2 = 1, 1
    if n < 0:
        print('please input a right number')
        return -1
    if n <= 2:
        return n
    while (n-2) > 0:
        a3 = a2+a1
        a1 = a2
        a2 = a3
        n = n-1

    print(a3)
    return a3

fabonacci(6)