class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        q = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        
        while len(q) != 0:
            n = q.popleft()
            for v in graph[n]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        for v in indegree:
            if v != 0:
                return False
        
        return True
or

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = collections.defaultdict(list)
        for des, src in prerequisites:
            adj[src].append(des)
        visit = [-1 for i in range(numCourses)]
        
        def dfs(node):
            if visit[node] == 0: return False
            if visit[node] == 1: return True
            visit[node] = 0 
            for nei in adj[node]:
                if not dfs(nei): return False 
            visit[node] = 1
            return True 
        for course in range(numCourses):
            if not dfs(course): return False 
        return True 
