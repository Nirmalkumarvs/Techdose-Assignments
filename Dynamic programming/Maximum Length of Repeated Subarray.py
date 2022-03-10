class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        r, c = len(nums1), len(nums2)
        dp = [[0]*(c + 1) for i in range(r + 1)] 
        max_len = -1
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                max_len = max(max_len, dp[i][j])
        return max_len
        
