class Solution(object):
    def nextPermutation(self, nums): 
        l=len(nums) 
        if l==1: 
            return
        i = l-2
        
        while(i>=0 and nums[i+1]<=nums[i]):
            i=i-1

        if(i>=0):
            c=1
            for j in range(i+1,len(nums)):
                if(nums[j]<=nums[i]):
                    c=0 
                    break
                    
            if c==0:
                temp=nums[j-1]
                nums[j-1]=nums[i]
                nums[i]=temp
    
                nums[i+1:]=nums[i+1:][::-1]
                
            else:
                temp=nums[len(nums)-1]
                nums[len(nums)-1]=nums[i]
                nums[i]=temp
               
                nums[i+1:]=nums[i+1:][::-1]

                
        
        else:         
            nums.reverse()
