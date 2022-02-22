class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[] 
        dic={} 
        l=len(nums2)
        for i in range(l-1,-1,-1): 
            k=nums2[i]
            while stack and stack[-1]<=k: 
                stack.pop(-1) 
            if stack: 
                dic[k]=stack[-1] 
            else: 
                dic[k]=-1 
            stack.append(k)
        res=[] 
        for i in nums1: 
            res.append(dic[i]) 
        return res[::]
