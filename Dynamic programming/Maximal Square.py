class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n, lgst = len(matrix), len(matrix[0]), 0
        hs=[[0]*(n+1) for i in range(m+1)] 
        for i in range(m): 
            for j in range(n): 
                hs[i+1][j+1]=int(matrix[i][j]) 
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                hs[i][j] *= min(hs[i - 1][j], hs[i - 1][j - 1], hs[i][j - 1]) + 1
                lgst = max(hs[i][j], lgst)
        for i in hs: 
            print(i)
        return lgst * lgst
