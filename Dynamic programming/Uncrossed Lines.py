class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        
        ans = [[0]*(l2+1) for _ in range(l1+1)]
        
        for i in range(l1):
            for j in range(l2):
                if nums1[i] == nums2[j]:
                    ans[i+1][j+1] = ans[i][j] + 1
                else:
                    ans[i+1][j+1] = max(ans[i+1][j], ans[i][j+1])
        
        return ans[-1][-1]
