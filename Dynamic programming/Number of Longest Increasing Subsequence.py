class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int: 
        dp = {} 
        res_len,res = 0 ,0
        n = len(nums) 
        for i in range(n-1,-1,-1):  
            max_len, max_count = 1, 1 
            
            for j in range(i+1,n):  
                
                if nums[j] > nums[i]: 
                    length, count = dp[j]
                    
                    if max_len < length + 1: 
                        max_len = length + 1 
                        max_count = count
                        
                    elif max_len == length + 1: 
                        max_count += count 
                        
            if max_len > res_len: 
                res_len = max_len  
                res = max_count
            elif max_len == res_len: 
                res += max_count  
                
            dp[i] = [max_len, max_count] 
            
        return res 
    
            
                
            
