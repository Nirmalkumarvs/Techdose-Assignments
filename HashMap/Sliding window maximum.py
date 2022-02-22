class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        deq=deque()
        res=[]
        for ind,val in enumerate(nums):
            while deq and nums[deq[-1]]<=val:
                deq.pop()
            deq.append(ind)
            
            
            if deq[0]==ind-k:
                deq.popleft()
    
            if ind>=k-1:
                res.append(nums[deq[0]])
        return res
