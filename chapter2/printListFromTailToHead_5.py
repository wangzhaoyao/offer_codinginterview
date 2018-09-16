# -*-coding:utf-8-*-
class ListNode:
    def __init__(self,data=None,next=None):
        self.val = data
        self.next = next

class Solution:
    def printTailToHead(listNode):
        out=[]
        if not listNode:
            return out
        phead=listNode

        while (phead !=None):
            out.append(phead.val)
            phead=phead.next
        out.reverse()
        return out
        # while listNode.next is not None:
        #     out.append(listNode.val)
        #     listNode=listNode.next
        # out.append(listNode.val)
        # out.reverse()
        # return out
listNode=ListNode(1,ListNode(3,ListNode(5,ListNode(7))))
s=Solution.printTailToHead(listNode)
print(s)
