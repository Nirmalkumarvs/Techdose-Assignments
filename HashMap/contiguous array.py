class Solution:
        def findMaxLength(self, nums: List[int]) -> int:
            dic = dict()
            dic[0] = -1
            count = 0
            maxL = 0
            for i in range(len(nums)):
                count += 1 if nums[i] == 1 else -1
                if count in dic:
                    maxL = max(maxL, i - dic[count])
                else:
                    dic[count] = i
            return maxL
