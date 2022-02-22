class Solution(object):
    def countBits(self, n): 
        c=[0]*(n+1)
        for i in range(1,n+1):  
            if i%2==0: 
                c[i]=c[i//2]
            else: 
                c[i]=c[i//2]+1
                
                
        return c[::]
