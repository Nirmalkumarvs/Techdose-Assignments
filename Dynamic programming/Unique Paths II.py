class Solution:
    def uniquePathsWithObstacles(self, m: List[List[int]]) -> int:  
        r,c=len(m),len(m[0])
        memo={}
        def paths(i,j): 
            key=(i,j) 
            if key in memo: 
                return memo[key]
            if i==1 and j==1 and m[i-1][j-1]!=1: 
                return 1 
            if i==0 or j==0 or m[i-1][j-1]==1: 
                return 0 
            memo[key]=paths(i-1,j)+paths(i,j-1) 
            return memo[key] 
        return paths(r,c)   
    
    ''' 
    if obstacleGrid[0][0]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                if obstacleGrid[i][j]==0:
                    if i==j==0: # dp[0][0]=1
                        dp[i][j] = 1
                        continue
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    '''
