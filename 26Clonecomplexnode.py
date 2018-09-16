#-*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
       self.label = x
       self.next = None
       self.random = None
"""
分三步：
第一步：复制每个节点，如：复制节点A得到A1，将A1插入节点A后面
第二步：遍历链表，A1->random = A->random->next;
第三步：将链表拆分成原链表和复制后的链表
"""


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        self.cloneNodes(pHead)
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)

    # 复制每个节点
    def cloneNodes(self, pHead):
        pNode = pHead
        while (pNode != None):
            # 每次随机分配一个新地址来存放待赋值节点的值
            pCloned = self.RandomListNode(pNode.label)
            pCloned.next = pNode.next
            pCloned.random = None

            pNode.next = pCloned
            pNode = pCloned.next

    # 遍历链表
    def ConnectSiblingNodes(self, pHead):
        pNode = pHead
        while (pNode != None):
            pCloned = pNode.next
            if (pNode.random != None):
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 将链表拆分成原链表和复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = None
        pClonedNode = None
        if (pNode != None):
            pClonedHead = pClonedNode = pNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        while (pNode != None):
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead