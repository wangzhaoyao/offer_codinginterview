# -*- coding:utf-8 -*-
class Solution:
    # 给定一个二叉树，获得其镜像（轴对称）的镜像二叉树：
    # 方式1：生成新的镜像二叉树
    def getMirrorBST(self, root):
        if root == None:
            return
        newTree = treeNode(root.val)
        newTree.right = self.getMirrorBST(root.left)
        newTree.left = self.getMirrorBST(root.right)
        return newTree
    # 方式2：改变给定的二叉树为镜像二叉树
    def turnToMirror(self, root):
        if root == None:
            return
        root.right, root.left = root.left, root.right
        self.turnToMirror(root.left)
        self.turnToMirror(root.right)
        return root


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
    flag = "turnToMirror"
    solution = Solution()
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    if flag == "mirrorBST":
        newRoot = solution.getMirrorBST(treeRoot1)
        print(newRoot)
    if flag == "turnToMirror":
        solution.turnToMirror(treeRoot1)
        print(treeRoot1)