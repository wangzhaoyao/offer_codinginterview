class ListNode:
    def __init__(self, x):
        self.val = None
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        p1 = head
        p2 = head
        for i in range(k-1):
            if p1.next == None:
                return None
            p1 = p1.next
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
        return p2


'''
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k<=0 or head==None:
            return None
        count=0
        p=head
        while p!=None:
            count=count+1
            p=p.next
        if count<k:
            return None
        number=count-k+1
        cnt=0
        p=head
        while p!=None:
            cnt=cnt+1
            if cnt==number:
                return p
            p=p.next
'''