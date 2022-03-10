class Solution:
    DIRS =[[ 0, -1 ], [ 0, 1 ], [ 1, 0 ], [ -1, 0 ]];
    def getFood(grid):
        m= len(grid)
        n = len(grid[0])
        queue=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="*":
                    queue.append([i,j])
                    break
                
        vis=set()
        step=0
        while queue:
            size = len(queue)
            for i in range(size):
                x,y = queue.pop(0)
                if grid[x][y]=='#':
                    return step
                for i,j in DIRS:
                    r = x+i
                    y = y+j
                    if r>=0 and r<m and c>=0 and c<n and grid[r][c]!='X' and (r,c) not in vis:
                        vis.add((i,j))
                        queue.append((r,c))

            step+=1
        return -1
        
