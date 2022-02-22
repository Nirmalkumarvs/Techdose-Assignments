class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])

        directn=[0,1,0,-1,0]
        visited=[]
        fresh,count=0,0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    visited.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        while visited and fresh:
            count+=1
            flag=0

            for j in range(len(visited)):
                r,c=visited.pop(0)
                for i in range(4):
                    nr,nc=r+directn[i],c+directn[i+1]
                    if nr<0 or nr==rows or nc<0 or nc==cols or grid[nr][nc]==0 or grid[nr][nc]==2: continue
                    grid[nr][nc]=2
                    fresh-=1
                    visited.append((nr,nc))
        if fresh>0:
            return -1
        return count
