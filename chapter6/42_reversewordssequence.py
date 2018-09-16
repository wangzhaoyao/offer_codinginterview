###思路一
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None or len(s) == 0:
            return s
        return " ".join(s.split(' ')[::-1])

###思路二
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None or len(s) == 0:
            return s
        stack = []
        for i in s.split(' '):
            stack.append(i)
        ans = ""
        while len(stack) > 0:
            ans += stack.pop() + " "
        ans = ans[:-1]
        return ans

###思路三
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None or len(s) == 0 or " " not in s:
            return s

        # 第一次翻转
        s = s[::-1]

        l = 0
        r = s.index(" ")

        ans = ""

        while r < len(s):
            # 第二次局部翻转
            ans += s[l: r][::-1] + " "

            l = r + 1
            r += 1

            while r < len(s) and s[r] != " ":
                r += 1

        ans += s[l: r][::-1]

        return ans