# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 思路一
    def FindFirstCommonNode1(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None

        s1 = []
        s2 = []
        p1 = pHead1
        p2 = pHead2
        while p1 is not None:
            s1.append(p1)
            p1 = p1.next
        while p2 is not None:
            s2.append(p2)
            p2 = p2.next

        res = None
        while len(s1) > 0 and len(s2) > 0:
            v1 = s1.pop()
            v2 = s2.pop()
            if v1 == v2:
                res = v1
            else:
                break
        return res

    # 思路二
    def getIntersectionNode2(self, headA, headB):
        # write your code here
        s1 = 0
        s2 = 0
        h1 = headA
        h2 = headB
        while h1 is not None:
            s1 += 1
            h1 = h1.next
        while h2 is not None:
            s2 += 1
            h2 = h2.next
        if s2 > s1:
            h2 = headB
            while s2 - s1 > 0:
                h2 = h2.next
                s2 -= 1
            h1 = headA
        elif s2 < s1:
            h1 = headA
            while s1 - s2 > 0:
                h1 = h1.next
                s1 -= 1
            h2 = headB
        else:
            h1 = headA
            h2 = headB
        res = None
        while h1 is not None and h2 is not None:
            if h1 == h2:
                res = h1
                return h1
            h1 = h1.next
            h2 = h2.next
        return res