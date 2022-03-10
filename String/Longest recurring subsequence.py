def findLongestRepeatingSubSeq(str):
    n = len(str)
  
    # Create and initialize DP table
    
    dp = [["" for k in range(n+1)] for l in range(n+1)]
  
    # Fill dp table (similar to LCS loops)
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            
            # If characters match and indices are not same
            if (str[i-1] == str[j-1] and i != j):
                dp[i][j] = dp[i-1][j-1] + str[i-1]
  
            # If characters do not match
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j],key=len)
  
    return dp[n][n]

s="AABEBCDD"
print(findLongestRepeatingSubSeq(s))
