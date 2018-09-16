import math
class Solution:
    def InversePairs(self, data):
        if not data:
            return False
        if len(data) == 1:
            return 0
        def merge(tuple_before, tuple_after):
            array_before = tuple_before[0]
            cnt_before = tuple_before[1]
            array_after = tuple_after[0]
            cnt_after = tuple_after[1]
            cnt = cnt_before+cnt_after
            flag = len(array_after)-1
            array_merge = []
            for i in range(len(array_before)-1,-1,-1):
                while array_before[i]<=array_after[flag] and flag>=0 :
                    array_merge.append(array_after[flag])
                    flag -= 1
                if flag == -1 :
                    break
                else:
                    array_merge.append(array_before[i])
                    cnt += (flag+1)
            if flag == -1 :
                for j in range(i,-1,-1):
                    array_merge.append(array_before[j])
            else:
                for j in range(flag ,-1,-1):
                    array_merge.append(array_after[j])
            return array_merge[::-1],cnt

        def mergesort(array):
            if len(array)==1:
                return (array,0)
            cut = math.floor(len(array)/2)
            tuple_before=mergesort(array[:cut])
            tuple_after=mergesort(array[cut:])
            return merge(tuple_before, tuple_after)
        return mergesort(data)[1]%1000000007

#instance
S=Solution()
array1=[1,2,3,2,1]
print ('inverse pairs of array1:',S.InversePairs(array1))

# array2=[5,4,3,2]
# print ('inverse pairs of array2:',S.InversePairs(array2))
#
# array3=[5,4,1,3,2]
# print ('inverse pairs of array3:',S.InversePairs(array3))
#
# array4=[364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
# print ('inverse pairs of array4:',S.InversePairs(array4))