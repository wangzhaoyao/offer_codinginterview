# _*_ encoding:utf-8 _*_

class ListNode:
    def __init__(self):
        self.value = None
        self.next_node = None


class Solution:
    def list_generate(self, lst):
        """
        传入一个列表将其生成链表
        """
        if not lst: # 列表为空
            return False
        node = ListNode()
        node.value = lst[0]
        if len(lst) == 1:
            node.next_node = None
        else:
            node.next_node = self.list_generate(lst[1:])
        return node

    def merge_list(self, head_node1, head_node2):
        """
        递增合并两个链表
        维持两个指针
        """
        if not head_node1:
            return head_node2
        elif not head_node2:
            return head_node1

        head_node = None

        if head_node1.value <= head_node2.value:
            head_node = head_node1
            head_node.next_node = self.merge_list(head_node1.next_node, head_node2)

        else:
            head_node = head_node2
            head_node.next_node = self.merge_list(head_node1, head_node2.next_node)

        return head_node

# 测试用例
if __name__ == '__main__':
    lst1_all = [[], [1], [1,3,5,7,9,11], [1,4,6,8,9,10,13]]
    lst2_all = [[], [1], [2], [1,3,4,6,7,10,11], [2,3,5,11,12,33]]

    for lst1 in lst1_all:
        for lst2 in lst2_all:
            solution = Solution()
            head_node1 = solution.list_generate(lst1)
            head_node2 = solution.list_generate(lst2)

            head_node = solution.merge_list(head_node1, head_node2)

            node = head_node
            # 打印链表
            print (lst1, lst2, )
            if node:
                while node:
                    print (node.value,)
                    node = node.next_node
                    if node:
                        print ('->',)
            else:
                print ('wrong')
            #print ('\n')




'''
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None: return l2
        if l2 is None: return l1
        new = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = new
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        else:
            if p1 is None:
                p3.next = p2
            else:
                p3.next = p1
        return new.next
'''