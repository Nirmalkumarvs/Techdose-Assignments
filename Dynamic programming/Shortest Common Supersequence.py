class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        dp = [['' for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
        lcm = dp[-1][-1]
        i, j = 0, 0
        res = ''
        for c in lcm:
            while i < n1 and str1[i] != c:
                res += str1[i]
                i += 1 
            while j < n2 and str2[j] != c:
                res += str2[j]
                j += 1 
            res += c 
            i += 1 
            j += 1 
        return res + str1[i : ] + str2[j : ]
