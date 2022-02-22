class Solution(object):
    def threeSum(self, nums): 
        length=len(nums)
        if(length<3): 
            return []
        nums.sort() 
        b=[] 
        [-4,-1,-1,0,1,2]
        for i in range(length-2):  
            if i==0 or nums[i]!=nums[i-1]: 
                l=i+1 
                r=length-1
                target=0-nums[i] 
                while l<r: 
                    twosum=nums[l]+nums[r] 
                    if twosum==target:  
                        b.append([nums[i],nums[l],nums[r]]) 
                        while l<r and nums[l]==nums[l+1]: 
                            l+=1 
                        while l<r and nums[r]==nums[r-1]: 
                            r-=1 
                        l+=1 
                        r-=1
                    elif twosum > target: 
                        r-=1 
                    else: 
                        l+=1
        return b
                    
                
