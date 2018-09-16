class Solution:
    def GetNumberOfK(self, data, k):
        left=0
        right=len(data)-1
        leftk=self.getleftK(data,k,left,right)
        rightk=self.getrightK(data,k,left,right)
        return rightk-leftk+1
    def getleftK(self,data,k,left,right):
        while left<=right:
            middle=(left+right)//2
            if data[middle]<k:
                left=middle+1
            else:
                right=middle-1
        return left
    def getrightK(self,data,k,left,right):
        while left<=right:
            middle=(left+right)//2
            if data[middle]<=k:
                left=middle+1
            else:
                right=middle-1
        return right