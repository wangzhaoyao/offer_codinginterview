# -*- coding:utf-8 -*-

from ctypes import *
def count(num):
    cnt = 0
    flag = 1
    while c_int(flag).value:
        if c_int(num & flag).value:
            cnt += 1
        flag = flag << 1
    return cnt



print(count(2))