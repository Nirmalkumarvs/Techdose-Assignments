class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        edges = dislikes
        from collections import defaultdict
        d = defaultdict(list)
        for k, v in edges:
            d[k].append(v)
            d[v].append(k)
            
        colors = {}
        
        def dfs(node):
            stack = [node]
            while stack:
                node = stack.pop()
                for nei in d[node]:
                    if nei not in colors:
                        if colors[node] == 0:
                            colors[nei] = 1
                        else:
                            colors[nei] = 0

                        stack.append(nei)
                    else:
                        if colors[nei] == colors[node]:
                            return False
            return True   
    
        for node in d:
            if node not in colors:
                colors[node] = 0
                if not dfs(node):
                    return False
        return True
                    
