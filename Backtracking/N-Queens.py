class Solution:
    def solveNQueens(self, n):
        col=set() 
        pdiag=set() 
        ndiag=set() 
        m=[['.']*n for i in range(n)] 
        res=[]
        def backtrack(r): 
            if r == n: 
                copy = [''.join(x) for x in m] 
                res.append(copy[::])
                return  
            
            for c in range(n): 
                if c in col or r+c in pdiag or r-c in ndiag: 
                    continue 
                
                col.add(c) 
                pdiag.add(r+c) 
                ndiag.add(r-c) 
                
                m[r][c]='Q' 
                
                backtrack(r+1) 
                
                col.remove(c) 
                pdiag.remove(r+c) 
                ndiag.remove(r-c)  
                
                m[r][c]='.' 
                
        backtrack(0) 
        
        return res
        
sol=Solution()
print(sol.solveNQueens(4))
