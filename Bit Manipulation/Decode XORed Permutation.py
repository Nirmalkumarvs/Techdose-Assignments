
class Solution(object):
    def decode(self, encoded): 
        al = 0
        total = 0 
        l=len(encoded)
        n = l + 1
        
        for i in range(l+1):
            total=total^(i+1)
            if i&1: 
                al=al^encoded[i]

        a = [al ^ total]

        for i in range(len(encoded)):
            a.append(encoded[i]^a[-1])

        return a
       
