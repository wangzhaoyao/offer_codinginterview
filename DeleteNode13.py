class ListNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None

class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None

        if pToBeDeleted.next != None: #如果要删除的节点后面不为空，则将下一个节点复制
            pToBeDeleted.val = pToBeDeleted.next.val
            pToBeDeleted.next = pToBeDeleted.next.next
            pToBeDeleted.next.__del__()
        elif pListHead == pToBeDeleted:
            pToBeDeleted.__del__()
            pListHead.__del__()
        else:
            pNode = pListHead
            while pNode != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()
