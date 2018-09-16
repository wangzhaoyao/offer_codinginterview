# 判断二叉树是否为平衡二叉树
# 先判断该节点是否平衡
# 再递归去判断左节点和右节点是否平衡

#方法一
# 递归求当前节点的深度
def getdepth(node):
    if not node:
        return 0
    ld = getdepth(node.left)
    rd = getdepth(node.right)
    return max(ld, rd) + 1


def isB(head):
    if not head:
        return True
    ld = getdepth(head.left)
    rd = getdepth(head.right)
    if abs(ld - rd) > 1:
        return False
    return isB(head.left) and isB(head.right)



#方法二
# 判断二叉树是否为平衡二叉树
# 先判断该节点是否平衡
# 再递归去判断左节点和右节点是否平衡
def process(head):
    if head is None:
        return True, 0
    leftData = process(head.left)
    if not leftData[0]:
        return False, 0
    rightData = process(head.right)
    if not rightData[0]:
        return False, 0
    if abs(leftData[1]-rightData[1]) > 1:
        return False, 0
    return True, max(leftData[1],rightData[1]) + 1

