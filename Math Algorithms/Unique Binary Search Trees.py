class Solution:
    def numTrees(self, n: int) -> int:
        cat_ = 1
        if n==1: 
            return cat_ 

        for i in range(1,n+1):
            cat_ *= (4 * i - 2);
            cat_ //= (i + 1); 
        
        return cat_
