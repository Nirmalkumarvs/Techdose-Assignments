class Solution:
    def longestPalindrome(self, s: str) -> str: 
        n=len(s) 
        ind = 0
        max_len=0
        for i in range(n): 
            l, r = i, i 
            
            while l>=0 and r<n and s[l] == s[r]:  
                length = r-l+1  
                if length > max_len: 
                    max_len = length 
                    ind = l
                l-=1 
                r+=1
                
            l, r = i, i+1  
            
            while l>=0 and r<n and s[l] == s[r]: 
                length = r-l+1  
                if length > max_len: 
                    max_len = length 
                    ind = l

                l-=1 
                r+=1  
        return s[ind:ind+max_len]
                
            
            
            
        
