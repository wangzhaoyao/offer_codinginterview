class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

def nonrecurse(head):              #循环的方法反转链表
    if head is None or head.next is None:
        return head
    pre=None
    cur=head
    #h=head
    while cur:
        h=cur
        tmp=cur.next
        cur.next=pre
        pre=cur
        cur=tmp
    return h

head=ListNode(1)   #测试代码
p1=ListNode(2)    #建立链表1->2->3->4->None;
p2=ListNode(3)
p3=ListNode(4)
head.next=p1
p1.next=p2
p2.next=p3
p=nonrecurse(head)  #输出链表 4->3->2->1->None
while p:
    print(p.val)
    p=p.next


# # !/usr/bin/env python
# # coding = utf-8
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# def rev(link):
#     pre = link
#     cur = link.next
#     pre.next = None
#     while cur:
#         temp = cur.next
#         cur.next = pre
#         pre = cur
#         cur = temp
#     return pre
#
#
# if __name__ == '__main__':
#     link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
#     root = rev(link)
#     while root:
#         print(root.data)
#         root = root.next