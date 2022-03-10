class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int: 
        r,c=len(dungeon),len(dungeon[0])
        
        for i in range(r-1,-1,-1): 
            for j in range(c-1,-1,-1): 
                if i==r-1 and j==c-1: 
                    dungeon[i][j] = min(0,dungeon[i][j]) 
                elif i==r-1: 
                    dungeon[i][j] = min(0, dungeon[i][j] + dungeon[i][j+1]) 
                elif j==c-1: 
                    dungeon[i][j] = min(0, dungeon[i][j] + dungeon[i+1][j])
                else: 
                    dungeon[i][j] = min(0, dungeon[i][j] + max(dungeon[i][j+1],dungeon[i+1][j]))  
        
        return abs(dungeon[0][0]) + 1
                
            
        
