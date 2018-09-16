class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def LastRemaining_Solution(self, n, m):
        if n == 0 or m == 0:
            return -1
        pHead = self.build_circle(n)
        step = 0
        while pHead:
            step += 1
            if step == m:

                if pHead.next != pHead:
                    pHead.val = pHead.next.val
                    pHead.next = pHead.next.next
                else:
                    print(pHead.val)
                    return
                step = 0
            else:
                pHead = pHead.next
        return

    def build_circle(self, n):
        tmp = None
        pHead = None
        pRear = None
        for i in range(n):
            if tmp == None:
                tmp = ListNode(i)
                pHead = tmp
            else:
                tmp.next = ListNode(i)
                tmp = tmp.next
        tmp.next = pHead
        return pHead


if __name__ == "__main__":
    double_num = input()
    n = int(double_num[0])
    m = int(double_num[1])
    so = Solution()
    so.LastRemaining_Solution(n, m)