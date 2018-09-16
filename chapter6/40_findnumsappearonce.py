class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        tagdict={}
        for i in array:
            if i in tagdict:
                tagdict[i]+=1
            else:
                tagdict[i]=1
        taglist=[]
        for j in tagdict:
            if tagdict[j]==1:
                taglist.append(j)
        return taglist


#方法二
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        taglist=[]
        for i in array:
            if array.count(i)==1 and i not in taglist:
                taglist.append(i)
        return taglist



#方法三：
class Solution(object):
    def findNumAPerOnce(self, data, length, num1, num2):
        if not data:
            return None
        resultOR = 0
        for i in range(length):
            resultOR = resultOR ^ data[i]
        indexOf1 = self.findFirstBitIs1(resultOR)
        for i in range(length):
            if self.isBit1(data[i], indexOf1):
                num1 = num1 ^ data[i]
            else:
                num2 = num2 ^ data[i]
        return num1, num2
    def findFirstBitIs1(self, num):
        indexBit = 0
        while num & 1 == 0:
            num = num >> 1
            indexBit = indexBit + 1
        return indexBit
    def isBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1

if __name__ == '__main__':
    nums = [2, 4, 3, 6, 3, 2, 5, 5]
    # nums = []
    target = 3
    print(Solution().findNumAPerOnce(nums, len(nums), 0, 0))