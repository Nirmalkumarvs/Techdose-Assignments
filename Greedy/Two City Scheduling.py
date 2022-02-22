class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs=sorted(costs,key=lambda x :(x[0]-x[1]))
        
        n=len(costs)
        
        ac=n//2
        ans=0
        
        for a,b in costs:
            if ac>0:
                ans+=a
                ac-=1
            else:
                ans+=b
        return ans
