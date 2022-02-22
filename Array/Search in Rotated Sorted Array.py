class Solution(object):
    def search(self, nums, target):
        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = int(low + (high-low) / 2)
            
            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[low]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    
