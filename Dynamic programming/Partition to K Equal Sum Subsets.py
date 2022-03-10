class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum = sum(nums)
        if k == 0 or totalSum % k != 0:
            return 0
        curSum, count, target = 0,0,totalSum//k
        
        nums.sort(reverse = True)
        taken = [False] * len(nums)
        
        def BT(start, curSum, count):
            if count == k - 1:
                return True
            if curSum == target:
                return BT(0,0,count+1)
            for i in range(start, len(nums)):
                if nums[i] + curSum <= target and (taken[i] == False):
                    taken[i] = True
                    if BT(i + 1 , curSum +nums[i] , count):
                        return True
                    taken[i] = False
            return False
        return BT(0, curSum, count)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    
        n = len(nums) 
        s  = sum(nums) 
        target = s//k 
        if s%k: 
            return False
        
        @lru_cache(None)
        def dp(mask,sets,curRemaining): 
            if mask==0 and sets==0: 
                return True
            
            for i in range(n): 
                if mask & (1<<i) != 0 and nums[i] <= curRemaining: 
                    newRemaining = curRemaining  - nums[i] 
                    if dp(mask ^ (1<<i), sets-1 if newRemaining==0 else sets, target if newRemaining==0 else newRemaining):
                        return True
                

        return dp(2**n-1,k,target)
