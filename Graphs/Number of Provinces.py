class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        n = len(isConnected)
        def dfs(start): 
            visit.add(start) 
            for end in range(n): 
                if end not in visit and isConnected[start][end]: 
                    dfs(end) 
        
            
        provinces = 0 
        visit = set() 
        for i in range(n): 
            if i not in visit:  
                provinces += 1
                dfs(i) 
        return provinces
        
