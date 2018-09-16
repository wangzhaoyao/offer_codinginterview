# -*- coding:utf-8 -*-

import numpy as np

def search(array, num):
    #搞清楚array的形状
    h=array.shape[0]-1
    w=array.shape[1]-1
    i=0

    if array[0][0] > num or array[h][w] < num:
        print("num is not in array")
        return

    while i<=h and w>=0:
        if array[i][w]==num:
            print("num is in array")
            return True
        elif array[i][w]>num:
            w=w-1
        else:
            i+=1
    print("num is not in array")
    return False



a = np.array([[1, 2, 8, 9],
     [2, 4, 9, 12],
     [4, 7, 10, 13],
     [6, 8, 11, 15]])
search(a, 5)