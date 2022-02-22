class Solution:
    def firstUniqChar(self, s: str) -> int: 
        d={} 
        for i,ii in enumerate(s): 
            if ii in d: 
                d[ii][0]+=1 
            else: 
                d[ii]=[1,i] 
        for i in d: 
            if d[i][0]==1: 
                return d[i][1] 
        return -1
        
