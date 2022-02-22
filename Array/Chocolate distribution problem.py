class Solution(object):
    def candy(self, ratings):
        l=len(ratings) 
        a=[1]*l  
        b=[1]*l
        for i in range(l-1): 
            if(ratings[i]<ratings[i+1]): 
                a[i+1]=a[i]+1  
            p=l-i-1
            if(ratings[p]<ratings[p-1]): 
                b[p-1]=b[p]+1  
        print(a) 
        print(b)
        for i in range(l): 
            a[i]=max(a[i],b[i]) 
        return sum(a)
