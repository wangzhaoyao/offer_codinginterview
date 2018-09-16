class Solution:
    def Add(self, num1, num2):
        while num2:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum
            num2 = carry
        return num1
print(Solution().Add(7,17))