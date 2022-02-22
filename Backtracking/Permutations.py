class Solution(object):
    def permute(self, nums):
       
        def comb(arr,n):  
            if n==0: 
                return [[arr[n]]] 
            else:  
                p=[]
                for j in comb(arr,n-1): 
                   
                    for k in range(n+1): 
                        r=j
                        r=r[:k]+[arr[n]]+r[k:]  
                        p.append(r)   
                return p
                        
                        
        return comb(nums,len(nums)-1)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
        ans = []
        backtrack(0, len(nums))
        return ans
