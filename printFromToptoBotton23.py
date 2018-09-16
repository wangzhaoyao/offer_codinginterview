# -*- coding:utf-8 -*-

class Solution:
   #从上往下打印出二叉树的每个节点，同层节点从左至右打印
    def PrintFromTopToBottom(self, root):
        array = []
        result = []
        if root == None:
            return result

        array.append(root)
        while array:
            newNode = array.pop(0)
            result.append(newNode.val)
            if newNode.left != None:
                array.append(newNode.left)
            if newNode.right != None:
                array.append(newNode.right)
        return result

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre)==0 | len(tin)==0:
            return None

        root = treeNode(pre[0])
        for order,item in enumerate(tin):
            if root .val == item:
                root.left = self.getBSTwithPreTin(pre[1:order+1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order+1:], tin[order+1:])
        return root

class treeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x

if __name__ == '__main__':
    flag = "printTreeNode"
    solution = Solution()
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    if flag == "printTreeNode":
        newArray = solution.PrintFromTopToBottom(treeRoot1)
        print(newArray)