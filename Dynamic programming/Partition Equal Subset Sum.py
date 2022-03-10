class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s, n, memo= sum(nums), len(nums), {0:True} 
        if s%2!=0: 
            return False
        nums.sort(reverse=True) 
        def dfs(i,x): 
            if x not in memo: 
                memo[x] = False 
                if x>0: 
                    for j in range(i,n): 
                        if dfs(j+1,x-nums[j]): 
                            memo[x] = True 
                            break 
            return memo[x] 
        return dfs(0, s>>1)
