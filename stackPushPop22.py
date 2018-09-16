# _*_encoding:utf-8 _*_


class Solution:

    def is_stack_push_list(self, list1, list2):
        length1 = len(list1)
        length2 = len(list2)

        if length1 != length2 or length1 == 0:
            return False

        p1_begin = 0
        p2_begin = 0
        # 模拟出入栈
        stack = []

        while True:
            number = list1[p1_begin]
            # 入栈
            stack.append(number)

            while stack and stack[-1] == list2[p2_begin]:
                # 当入栈的元素与list2的当前元素相同，则出栈，并且p2指向下一个
                stack.pop()
                p2_begin += 1

            if p1_begin == length1-1:
                # 当p1指向最后一个元素时，模拟出入栈已经结束，如果list2表示正确的出栈顺序，那么stack应该为空
                if stack:
                    return False
                else:
                    return True
            p1_begin += 1

if __name__=="__main__":
    list1=[1,2,3,4,5]
    list2=[4,5,3,2,1]
    A=Solution()
    print(A.is_stack_push_list(list1,list2))