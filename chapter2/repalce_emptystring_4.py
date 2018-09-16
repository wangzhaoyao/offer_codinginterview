class Solution(object):
    def replaceSpace(self,s):
        strlen=len(s)
        if strlen==0:
            print("please input a string that contains space")
        else:
            newstr=[]
            for i in range(strlen):
                if s[i]==' ':
                    newstr.append("%20")
                else:
                    newstr.append(s[i])
            string="".join(newstr)
            return string


solution=Solution()
str_test="we are family"
print(solution.replaceSpace(str_test))
