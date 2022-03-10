class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        r, c = len(text1), len(text2)
        dp=[[0]*(c+1) for i in range(r+1)] 
        for i in range(r+1): 
            for j in range(c+1): 
                if i==0: 
                    dp[i][j] = j 
                    continue
                if j==0: 
                    dp[i][j] = i 
                    continue
                    
                if text1[i-1] == text2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] 
                else: 
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) 
        
        return dp[-1][-1]
        
