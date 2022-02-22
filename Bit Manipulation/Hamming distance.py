class Solution(object):
    def hammingDistance(self, x, y): 
        a=[0]*32
        b=[0]*32 
        p=0
        while(x): 
            a[p]=(x&1) 
            x=x>>1 
            p+=1
        p=0
        while(y): 
            b[p]=(y&1) 
            y=y>>1
            p+=1
        
        return sum([a[i]!=b[i] for i in range(32)])
