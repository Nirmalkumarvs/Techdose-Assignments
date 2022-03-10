m=[[4,2,9,6,1],
   [7,9,6,5,4],
   [5,7,3,8,8],
   [7,4,9,9,4]]

r=len(m)
c=len(m[0])

dp=[[0]*(c+1) for  i in range(r+1)]
dp2=[[0]*(c) for i in range(r)]

for i in range(1,r+1):
    for j in range(1,c+1):
        dp[i][j]=m[i-1][j-1]+max(dp[i-1][j],dp[i][j-1])

# top right t0 bot left
dp2[0][c-1]=m[0][c-1]
for j in range(c-2,-1,-1):
    dp2[0][j] = dp2[0][j+1] + m[0][j]
for i in range(1,r):
    dp2[i][-1]= dp2[i-1][-1] + m[i][-1]
    
for i in range(1,r):
    for j in range(c-2,-1,-1):
       dp2[i][j]=m[i][j] + max(dp2[i-1][j],dp2[i][j+1])

for i in dp2:
    print(*i)
        
