class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        cache={}
        lenS,lenP=len(s),len(p)
    
        def dfs(i,j):
            
            if (i,j) in cache:
                return cache[(i,j)]
            if i>=lenS and j>=lenP:
                return True
            if j>=lenP:
                return False
        
            match=i<lenS and (s[i]==p[j] or p[j]=='.')
            
            if (j+1)<lenP and p[j+1]=="*":
                cache[(i,j)]=dfs(i,j+2) or (match and dfs(i+1,j))
            elif match:
                cache[(i,j)]=dfs(i+1,j+1)
            else:
                cache[(i,j)]=False
            return cache[(i,j)]
    
        return dfs(0,0)
