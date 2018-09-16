# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        zeros = numbers.count(0)
        gaps = 0
        small = zeros
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            gaps += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return gaps <= zeros