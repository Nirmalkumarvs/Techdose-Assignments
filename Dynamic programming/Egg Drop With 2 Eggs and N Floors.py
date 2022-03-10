class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = []
        move = 1
        while len(dp) < n:
            for move_range in range(move):
                dp.append(move)
            move += 1 
        print(dp)
        return dp[n-1] 
    #or
    def twoEggDrop(self, n: int) -> int:
        nn= (-1.0+sqrt(1+8*n))/2.0;
        return nn+(nn*(nn+1)==n*2?0:1);
    #or
    
    def twoEggDrop(self, n: int) -> int:
        i = 0
        max_cover = i*(i+1) // 2
        while max_cover < n:
            i += 1
            max_cover = i*(i+1) // 2
        return i
