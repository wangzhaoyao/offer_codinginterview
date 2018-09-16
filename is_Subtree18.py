# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    #判断 单个root的子树的程序
    def isSubtree(self, root1, root2):
        #如果2遍历完说明 匹配成功
        if root2 == None:
            return True
        #如果1便利完说明，2还没便利完，匹配不成功
        if root1 == None:
            return False
        #如果这对根节点的值相等，进行相应的递归遍历这对节点的 左右节点是否匹配
        if root1.val == root2.val:
            return self.isSubtree(root1.left,root2.left) and self.isSubtree(root1.right,root2.right)
    #总程序
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        #特殊情况 需判断
        if pRoot1 == None or pRoot2 == None:
            return False
        #进行递归判断和遍历，判断1此时是否有2的子树，或1的左子树中是否存在与2相同的的子树，或1的右子树是否存在与2相同的子树
        return self.isSubtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)