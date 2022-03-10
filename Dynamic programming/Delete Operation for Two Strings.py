class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r, c = len(word1), len(word2)
        dp=[[0]*(c+1) for i in range(r+1)] 
        for i in range(1,r+1): 
            for j in range(1,c+1): 
                if word1[i-1] == word2[j-1]: 
                    dp[i][j] = 1 + dp[i-1][j-1] 
                else: 
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 
        
        return r + c - 2*dp[-1][-1]
        
