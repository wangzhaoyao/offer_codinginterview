# -*-coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):

        self.list = []
        self.list1 = []

    def FindPath(self, root, expectNumber):
        if root == None:
            return self.list1
        # print('********')
        self.list.append(root.val)
        # print(list)
        expectNumber -= root.val
        # print('----', target)
        if expectNumber == 0 and root.left == None and root.right == None:
            newlist = []
            for line in self.list:
                newlist.append(line)
            self.list1.append(newlist)
        # print('*****', list1)
        # list1.append(proot.val)
        # print(list1)
        # print(list)
        # print('********')
        # print(proot.val)
        # print('********')

        self.FindPath(root.left, expectNumber)

        self.FindPath(root.right, expectNumber)
        self.list.pop()
        return self.list1
