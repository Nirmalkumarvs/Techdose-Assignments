class Solution:
    def criticalConnections(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = [[] for _ in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = [False]*n
        low = [None]*n
        time = [None]*n
        t = [0]
        res = []
        
        
        def dfs(node,parent=None):
            seen[node] = True
            low[node] = time[node] = t[0]
            t[0] += 1
    
            for nei in graph[node]:
                if parent == nei:
                    continue
                if seen[nei]:
                    low[node] = min(low[node],time[nei])
                else:
                    dfs(nei,node)
                    low[node ] = min(low[node],low[nei])
                    if low[nei] > time[node]:
                        res.append([node,nei])
                
        for i in range(n):
            if seen[i] == False:
                dfs(i)
        return res
