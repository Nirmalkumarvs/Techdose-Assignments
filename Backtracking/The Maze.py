def haspath(maze,start,dest):
    m,n,vis=len(maze),len(maze[0]),set()
    def dfs(x,y):
        if (x,y) in vis:
            return False
        else:
            vis.add((x,y))

        if [x,y] == dest:
            return True
        
        for i, j in (0,-1),(0,1),(1,0), (-1,0):
            nx,ny=x,y
            while 0<= nx+i < m and 0<=ny+j<n and maze[nx+i][ny+j]!=1:
                nx += i
                ny += j
            if dfs(nx,ny):
                return True
            
        return False
    return dfs(*start)
            
