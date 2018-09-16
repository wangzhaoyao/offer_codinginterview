# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        res = ''.join(self.sorted(list(map(str, numbers)))).lstrip('0')
        return res or '0'
    def sorted(self,numbers):
        if len(numbers) == 0:
            return []
        x = numbers[0]
        return self.sorted([i for i in numbers[1:] if i+x < x+i ]) + [x] + self.sorted([i for i in numbers[1:] if i+x >= x+i])

nums=[123,45,0]
s=Solution()
print(s.PrintMinNumber(nums))