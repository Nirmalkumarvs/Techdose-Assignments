class Solution(object):
    def uniquePaths(self, m, n):
        
        def dp(m , n , look = {}):
            
            if m == 1 or n == 1:
                return 1
            if m == 0 or n == 0:
                return 0
        
            if (m,n) in look:
                return look[(m,n)]
        
            else:
                look[(m,n)] = dp(m-1 , n , look) + dp(m , n-1 , look)
                return look[(m,n)]
            
        return dp(m , n , look = {}) 
        
        '''
        numWays = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                numWays[i][j] = numWays[i][j-1]+numWays[i-1][j]
                
        return numWays[m-1][n-1] 
        
        '''
