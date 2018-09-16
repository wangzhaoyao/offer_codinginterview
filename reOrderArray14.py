class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) < 1:
            return []
        elif len(array) == 1:
            return array

        low = 0
        high = len(array)-1
        while low <= high:
            if array[low] & 1 == 1: # array[low]%2 == 1
                low = low + 1
            if array[high] & 1 == 0:
                high = high - 1
            if low < high:
                s = array[low]
                array[low] = array[high]
                array[high] = s
        return array

a=Solution()
arr=[1,3,4,5,8,9,6]
print(a.reOrderArray(arr))

#辅助空间法
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        left = [x for x in array if x & 1 == 1]
        right = [x for x in array if x & 1 == 0]
        return left + right
'''