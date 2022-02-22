class Solution(object):     
    def majorityElement(self, arr): 
    
        val = arr[0]
        count = 1
        freq = 0
        n = len(arr) 
        for i in range(1,n): 
            if arr[i]==val: 
                count+=1 
            else:
                count-=1 
            if count==0: 
                val=arr[i] 
                count=1 
                
        return val;
