class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        
        check = defaultdict(int)
        
        for a in nums1:
            for b in nums2:
                check[a+b] += 1
        
        ans = 0
        
        for c in nums3:
            for d in nums4:
                ans += check[-(c+d)]
                    
    
        return ans
        
        
