class Solution(object):
    def maxProfit(self, prices):
        buy,sell,maxp=prices[0],prices[0],0 
        for i in prices: 
            if i < buy: 
                buy=i 
                sell=i 
                continue
            if i > sell: 
                if i-buy > maxp: 
                    maxp=i-buy 
                    sell=i 
        return maxp
        
