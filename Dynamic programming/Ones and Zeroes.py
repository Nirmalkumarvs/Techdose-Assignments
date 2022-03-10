class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache 
        
        def dp(i, m, n):
            if i == len(strs): 
                return 0
            
            numOnes = numZeroes = 0
            
            for c in strs[i]:
                if c == '0': numZeroes += 1
                else: numOnes += 1 
                    
            if m-numZeroes >= 0 and n-numOnes >= 0: 
                return max(dp(i+1, m, n), 1 + dp(i+1, m-numZeroes, n-numOnes))
            else:
                return dp(i+1, m, n) 
            
        return dp(0, m, n)
'''
class Solution:
	def findMaxForm(self, s,zero , one):# List[str], m: int, n: int) -> int:
		
		def f(x,y,z):
			k=0
			for i in x:
				if i.count('0')<=y and i.count('1')<=z:
					k+=1
					y-=i.count('0')
					z-=i.count('1')
			return k

		s_len=sorted(s,key=lambda x: (len(x), x.count('0')))
		s_0=sorted(s,key=lambda x: x.count('0'))
		s_1=sorted(s,key=lambda x: x.count('1'))		
		
		return max(f(s_len,zero,one), f(s_0,zero,one), f(s_1,zero,one))
		
'''
