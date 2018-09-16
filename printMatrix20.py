# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while(matrix):
            result+=matrix.pop(0)#取第一行放入result，并删除第一行
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result
    def turn(self,matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):#将j和i反过来，变为转置矩阵
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()#调换转置矩阵的顺序，变为魔方旋转
        return newmat

print("---------------------------------------------------------------")

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        if m==1 and n==1:
            res=[matrix[0][0]]
            return res
        else:
            for o in range((min(m,n)+1)//2):
                [res.append(matrix[o][i]) for i in range(o,m-o)]
                [res.append(matrix[j][m-o-1]) for j in range(o,n-o) if matrix[j][m-o-1] not in res]
                [res.append(matrix[n-o-1][k]) for k in range(m-1-o,o-1,-1) if matrix[n-o-1][k] not in res]
                [res.append(matrix[l][o]) for l in range(n-1-o,o-1,-1) if matrix[l][o] not in res]
            return res





