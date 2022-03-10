import bisect
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def LIS(nums): 
            dp = [] 
            for num in nums: 
                index = bisect.bisect_right(dp,num) 
                if index == len(dp): 
                    dp += [num] 
                else: 
                    dp[index] = num 
            return len(nums) - len(dp) 
        
                
        groups = [[] for _ in range(k)]
        
        for i, a in enumerate(arr):
            groups[i%k] += [a]
        
        cnt = 0
        for group in groups:
            cnt += LIS(group)
            
        return cnt
