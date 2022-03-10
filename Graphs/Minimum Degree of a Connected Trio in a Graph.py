class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set) 
        for u, v in edges: 
            g[u].add(v)
            g[v].add(u)
            
        ans = float('inf') 
        node_degree = sorted([[len(g[k]), k] for k in g])
        for a, b in edges: 
            w = len(g[a]) + len(g[b])
            for w1, c in node_degree: 
                if c in g[a] and c in g[b]: 
                    ans = min(ans, w1 + w-6) 
                    break 
        return ans  if ans != float('inf') else -1
