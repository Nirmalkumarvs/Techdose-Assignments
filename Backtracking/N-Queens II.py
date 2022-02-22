class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set() 
        pdiag=set() 
        ndiag=set() 
       
        def backtrack(r): 
          
            if r == n: 
                return  1
            
            sol=0
            for c in range(n): 
                if c in col or r+c in pdiag or r-c in ndiag: 
                    continue 
                
                col.add(c) 
                pdiag.add(r+c) 
                ndiag.add(r-c) 
                
                sol+=backtrack(r+1) 
                
                col.remove(c) 
                pdiag.remove(r+c) 
                ndiag.remove(r-c)  
                
            return sol
                
        return backtrack(0) 
