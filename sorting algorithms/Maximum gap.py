class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        lenNum=len(nums)
        if lenNum<2:
            return 0
    
        maximum,minimum=max(nums),min(nums)
        numOfBuckets=lenNum-1
        bucketSize=math.ceil((maximum-minimum)/numOfBuckets)

        minBucket=[float("inf")]*numOfBuckets
        maxBucket=[-1]*numOfBuckets
    
        for num in nums:
            if num==minimum or num==maximum:
                continue
            index=(num-minimum)//bucketSize
            maxBucket[index]=max(maxBucket[index],num)
            minBucket[index]=min(minBucket[index],num)
        
        prev=minimum
        maxGap=0
    
        for i in range(len(minBucket)):
            if maxBucket[i]==-1:
                continue
            maxGap=max(maxGap,minBucket[i]-prev)    
            prev=maxBucket[i]
    
        maxGap=max(maxGap,maximum-prev)
    
        return maxGap
