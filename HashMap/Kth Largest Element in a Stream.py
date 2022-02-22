class KthLargest:

    def __init__(self, k, nums):
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        self.hp = nums
        self.k = k

    def add(self, val):
        if len(self.hp) < self.k:  
            heapq.heappush(self.hp, val)
        elif val > self.hp[0]:  
            heapq.heapreplace(self.hp, val)
        return self.hp[0]
