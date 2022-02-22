class NumArray(object):

    def __init__(self, nums):
        self.l=len(nums)
        self.a=[0]*self.l  
        self.a[0]=nums[0]
        for i in range(1,self.l): 
            self.a[i]+=(self.a[i-1]+nums[i])

    def sumRange(self, left, right): 
        if left==0: 
            return self.a[right]
        return self.a[right]-self.a[left-1]
        
