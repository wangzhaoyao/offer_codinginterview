# -*- coding:utf-8 -*-
from functools import reduce
class Solution:
    def Sum_Solution(self, n):
        # write code here
        def f(x,y):
            return x+y
        return reduce(f,range(1,n+1))



# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and (n+self.Sum_Solution(n-1))