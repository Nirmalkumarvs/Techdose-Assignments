class Solution:
    def maxCoins(self, nums: List[int]) -> int: 
        nums = [1]+nums+[1] 
        n = len(nums)
        dp = [ [0]*n for _ in range(n) ]

        for window in range(1,n+1):                           
            for left in range(n-window+1):                    
                right = left + window - 1                             
                for last in range(left+1,right):                      
                    dp[left][right] = max( dp[left][right] , dp[left][last] + nums[left]*nums[last]*nums[right]+ dp[last][right] )
        return dp[0][len(nums)-1]
