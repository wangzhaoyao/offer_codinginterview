# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        small, big = 1, 2
        _len = (tsum + 1) / 2
        curr = small + big
        res = []
        while small < _len:
            if curr == tsum:
                res.append(range(small, big + 1))
            while curr > tsum and small < _len:
                curr -= small
                small += 1
                if curr == tsum:
                    res.append(range(small, big + 1))
            big += 1
            curr += big
        return res