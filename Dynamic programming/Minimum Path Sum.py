class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:  
        memo={}
        def minpath(i,j): 
            key=(i,j) 
            if i==0 and j==0: 
                return grid[i][j] 
            if i==-1 or j==-1:
                return float("inf")
            if key in memo: 
                return memo[key] 
            else:
                memo[key] = grid[i][j] + min(minpath(i-1,j),minpath(i,j-1)) 
                return memo[key] 
        return minpath(len(grid)-1,len(grid[0])-1) 
    
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1,len(grid)):
            grid[i][0]+=grid[i-1][0]
        for j in range(1,len(grid[0])):
            grid[0][j]+=grid[0][j-1]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
    
    '''
        
