class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int: 
        s=0 
        m=0
        time=0
        for i in range(len(colors)): 
            if(i>0 and colors[i]!=colors[i-1]): 
                time+=(s-m) 
                s=0  
                m=0 
            s+=neededTime[i] 
            m=max(m,neededTime[i]) 
        
        time += (s-m)
        return time
                
