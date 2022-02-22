class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """ 
        nums.sort() 
        t=[]
        length=len(nums) 
        if length<4: 
            return []  
        for i in range(length-3): 
            if i>0 and nums[i]==nums[i-1]: 
                continue
            for j in range(i+1,length-2):  
                if j>i+1 and nums[j]==nums[j-1]: 
                    continue 
                l=j+1 
                r=length-1 
                tar=target-(nums[i]+nums[j]) 
                while l<r: 
                    twosum=nums[l]+nums[r] 
                    if twosum==tar:  
                        k=([nums[i],nums[j],nums[l],nums[r]]) 
                         
                        t.append(k)
                
                        while l<r and nums[l]==nums[l+1]: l+=1 
                        while l<r and nums[r]==nums[r-1]: r-=1 
                        l+=1 
                        r-=1 
                    elif twosum>tar: 
                        r-=1 
                    else: 
                        l+=1 
        return t
                        
                
        
        
