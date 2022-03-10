class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: 
        n = len(heights) 
        l,r = [0]*n,[0]*n  
        
        stack=[]
        for i in range(n):  
            while stack and heights[stack[-1]]>=heights[i]: 
                stack.pop()  
            l[i] = stack[-1] if stack else -1 
            stack.append(i)  
        stack=[]
        for i in range(n-1,-1,-1):  
            while stack and heights[stack[-1]]>=heights[i]: 
                stack.pop() 
            r[i] = stack[-1] if stack else n
            stack.append(i)  
        stack=[] 
        
        return max([heights[i]*(r[i]-l[i]-1) for i in range(n)])
            
            
        
