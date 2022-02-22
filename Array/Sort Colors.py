class Solution(object):
    def sortColors(self, nums):
        i, l, r = 0, 0, len(nums)-1
        while i<=r:
            if nums[i]==0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1 
            if nums[i]==2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                continue
            i += 1
        return nums
