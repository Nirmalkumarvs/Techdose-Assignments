class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        k = (len1 + len2) // 2
        low, high = 0, len1
        
        while low <= high:
            cut1 = low + (high - low) // 2
            cut2 = k - cut1
            
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            
            r1 = float('inf') if cut1 == len1 else nums1[cut1]
            r2 = float('inf') if cut2 == len2 else nums2[cut2]
            
            if l1 > r2:
                high = cut1 - 1
            elif l2 > r1:
                low = cut1 + 1
            else:
                if (len1 + len2) % 2 != 0:
                    return (float)(min(r1, r2))
                
                return (max(l1,l2) + min(r1,r2)) / 2
            
        return 0.0
