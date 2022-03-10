class Solution:
    def findTargetSumWays(self, nums: [int], target: int) -> int:
        n = len(nums)
        s = sum(nums)  
        if s<target: 
            return 0 
        
        
        @lru_cache(None)
        def bt(index,s): 
            
            if index==n: 
                return 1 if s==target else 0 
            
            return bt(index+1,s-nums[index])+bt(index+1,s+nums[index])
        
        return bt(0,0)
    
        
            
