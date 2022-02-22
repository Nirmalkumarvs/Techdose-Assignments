class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height.copy()
        right_max = height.copy()
        lm = height[0]
        rm = height[-1]
        
        for i in range(len(height)):
            left_max[i] = max(lm, height[i])
            if left_max[i] != lm:
                lm = left_max[i]
        
        for j in range(len(height)-1, 0, -1):
            right_max[j] = max(rm, height[j])
            if right_max[j] != rm:
                rm = right_max[j]
        
        
        ans = 0
        for i in range(len(height)):
            ans += min(right_max[i], left_max[i]) - height[i]
        
        return ans        
