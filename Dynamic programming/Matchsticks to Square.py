class Solution:
    
    def makesquare(self, matchsticks: List[int]) -> bool:  
        k=4
        n = len(matchsticks) 
        s  = sum(matchsticks) 
        target = s//k 
        if s%k: 
            return False
        
        @lru_cache(None)
        def dp(mask,sides,curRemaining): 
            if mask==0 and sides==0: 
                return True 
            for i in range(n): 
                if mask & (1<<i) != 0 and matchsticks[i] <= curRemaining: 
                    newRemaining = curRemaining  - matchsticks[i] 
                    if dp(mask ^ (1<<i), sides-1 if newRemaining==0 else sides, target if newRemaining==0 else newRemaining):
                        return True
                

        return dp(2**n-1,4,target)
        
