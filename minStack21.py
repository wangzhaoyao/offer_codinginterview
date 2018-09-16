# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node) #如果新压入的值比最小值小，则向辅助栈压入新值，否则压入最小值
        if self.min_stack == [] or node < self.min():
            self.min_stack.append(node)
        else:
            temp = self.min()
            self.min_stack.append(temp)

    def pop(self):
        # 只要不为空就删除原始栈和辅助栈的元素
        if self.min_stack == [] or self.stack == []:
            return None
        self.min_stack.pop()
        self.stack.pop()

    def top(self):#返回栈顶
        # write code here
        return self.stack[-1]

    def min(self):
        # 返回当前最小值
        return self.min_stack[-1]


if __name__ == '__main__':
    stack = Solution()
    stack.push(2)
    stack.push(1)
    stack.push(3)
    stack.push(4)
    print(stack.min())