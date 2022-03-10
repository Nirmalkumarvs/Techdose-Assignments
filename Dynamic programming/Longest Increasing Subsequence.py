class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:     
        track = []
        for n in nums:
            if not track or n > track[-1]:
                track.append(n)
                continue
            ind = bisect_left(track, n)
            track[ind] = n 
            
        return len(track) 
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        tails = [0] * n
        tails[0] = nums[0]
        
        size = 0
        for num in nums:
            l, r = 0, size-1
            while l <= r:
                mid = (l+r)//2
                if tails[mid] >= num:
                    r = mid - 1
                else:
                    l = mid + 1

            tails[l] = num
            size = max(size, l+1)
            
        return size 
    ''' 
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:     
        n=len(nums)
        LIS = [1]*n  
        for i in range(n-1,-1,-1): 
            for j in range(i+1,n): 
                if nums[j]>nums[i]: 
                    LIS[i] = max(LIS[i], 1 + LIS[j] 
        return max(LIS)
    '''
    
