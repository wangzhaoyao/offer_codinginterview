class Solution:
    def __init__(self):
        self.result = []
    def Permutation(self, ss):
        s = list(ss)
        # to = len(ss)
        # for i in range(to):
        #     s.append(ss[i])
        self.PermutationHelper(s, 0, len(ss))
        self.result = list(set(self.result))
        self.result.sort()
        return self.result
    def PermutationHelper(self, ss, fro, to):
        if (to <= 0):
            return
        if (fro == to - 1):
            self.result.append(''.join(ss))
        else:
            for i in range(fro, to):
                self.swap(ss, i, fro)
                self.PermutationHelper(ss, fro + 1, to)
                self.swap(ss, fro, i)
    def swap(self, str, i, j):
        str[i], str[j] = str[j], str[i]
a=list('abad')
s=Solution()
print(s.Permutation(a))