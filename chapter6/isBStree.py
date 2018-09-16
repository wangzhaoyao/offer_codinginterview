# 二叉搜索树
# 中序遍历情况下，值递增则为二叉树
def isBSTree(head):
    minimum = -100000               # 设定一个最小值
    if head is None:
        return False
    prenum = minimum
    stack = []
    while head or len(stack) > 0:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            if head.val < prenum:   # 保证中序遍历情况下值递增
                return False
            else:
                prenum = head.val
            head = head.right
    return True