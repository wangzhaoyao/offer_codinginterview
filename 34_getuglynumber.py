# -*- coding:utf-8 -*-

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <=0:
            return 0
        ans = [1]
        i2,i3,i5 = 0,0,0
        i = 1
        while len(ans)<index:
            ans.append(min(ans[i2]*2,min(ans[i3]*3,ans[i5]*5)))
            # 要分别比较，不能直接用elif ,这样的话有一些相同的值会重复比较
            if ans[i] == ans[i2]*2:
                i2 +=1
            if ans[i] == ans[i3]*3:
                i3 +=1
            if ans[i] == ans[i5]*5:
                i5 +=1
            i +=1
        return ans[i-1]
s=Solution()
print(s.GetUglyNumber_Solution(1500))