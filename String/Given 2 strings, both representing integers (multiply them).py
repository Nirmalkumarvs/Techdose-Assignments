class Solution(object):
    def multiply(self, num1, num2):
        initial = 48
        def converter(nums):
            ones = 1
            res = 0
            for i in nums[::-1]:
                res += ones * (ord(i) - initial)
                ones *= 10
            return res
        return str(converter(num1) * converter(num2))
        
        
