class Solution:
    def canJump(self, nums: List[int]) -> bool:
	    
        reachable = 0 
        n = len(nums) 
        for i in range(n): 
            if reachable < i: 
                return False 
            reachable=max(reachable,nums[i]+i) 
            
        return True
