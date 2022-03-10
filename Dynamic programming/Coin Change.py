class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dp(coins, amount):
            if amount < 0: 
                return -1
            if amount == 0: 
                return 0
            if amount in memo:
                return memo[amount]
            
            res = float("inf")
            
            for coin in coins:
                cur_sol = dp(coins, amount-coin)
                if cur_sol != -1:
                    res = min(res, cur_sol+1) 
                    
            memo[amount] = -1 if res == float("inf") else res
            return memo[amount]

        return dp(coins, amount)
