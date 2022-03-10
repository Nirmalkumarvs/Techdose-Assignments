class Solution:
    def change(self, amount: int, coins: List[int]) -> int: 
        n = len(coins)
        coins.sort(reverse=True) 
        
        memo={}
        def bt(ind,cur_sum):  
            key = (ind,cur_sum)
            if key in memo: 
                return memo[key]
            if cur_sum==0:  
                memo[key] = 1
                return 1 
            if cur_sum<0:  
                memo[key] = 0
                return 0 
            sum = 0
            for i in range(ind,n): 
                sum += bt(i,cur_sum - coins[i])  
            memo[key] = sum
            return sum 
        return bt(0,amount)
                    
        
    def change1(self, amount: int, coins: List[int]) -> int: 
        res=[0]*(amount+1) 
        res[0]=1
        for coin in coins: 
            for i in range(coin,amount+1): 
                res[i] += res[i-coin]  
        return res[-1]
                
    
    def change2(self, amount: int, coins: List[int]) -> int:
        m=len(coins)
        dp=[[0 for i in range(amount+1)] for j in range(m+1)]
        
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,amount+1):
            dp[0][i]=0
            
        for i in range(1,m+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=dp[i][j-coins[i-1]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
                    
        return dp[m][amount]
    '''
