class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums)<1: return None
        if len(nums)==1: return nums if nums[0]==k else None
        
        counts = collections.Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)
