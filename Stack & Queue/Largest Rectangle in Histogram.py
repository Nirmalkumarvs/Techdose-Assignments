class Solution:
  
    def largestRectangleArea(self, heights: List[int]) -> int:
        sz = len(heights)
        left = [-1 for i in range(sz)]
        right = [-1 for i in range(sz)]
        stack = []
        max_area=0
       
        
        def fill_left(i):
            while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()
            if len(stack)==0:
                left[i]=0
                stack.append(i)
            else:
                left[i]=stack[-1]+1
                stack.append(i)
            return
        
        
        def fill_right(j):
            while len(stack)>0 and heights[stack[-1]]>=heights[j]:
                    stack.pop()
            if len(stack)==0:
                right[j]=sz-1
                stack.append(j)
            else:
                right[j]=stack[-1]-1
                stack.append(j)
            return
       
        for i in range(sz):
            fill_left(i)
        stack=[]
        for i in range(sz):
            fill_right(sz-i-1)
         
       
        for i in range(sz):
            max_area=max(max_area, (right[i]-left[i]+1)*heights[i])
        return max_area
