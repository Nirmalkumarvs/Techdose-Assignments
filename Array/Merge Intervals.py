class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:(x[0],x[1]))  
        k=0  
        start=intervals[0][0]
        end=intervals[0][1]  
        
        for i in intervals[1:]:  
            if i[0]<=end: 
                end=max(i[1],end) 
            else: 
                intervals[k]=[start,end] 
                k+=1
                start=i[0] 
                end=i[1] 
        intervals[k]=[start,end]
        return intervals[:k+1]
            
        
