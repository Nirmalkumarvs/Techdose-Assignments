class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        indegrees = [0] * numCourses
        queue = deque([])
        res = []
        visited = set()
        
        for x, y in prerequisites:
            graph[y].append(x)
            indegrees[x] += 1

        for i, x in enumerate(indegrees):
            if x == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            res.append(node)
            visited.add(node)
            
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                
            for i, x in enumerate(indegrees):
                if x == 0 and i not in visited:
                    queue.append(i)
            
        for x in indegrees:
            if x > 0:
                return []
        return res





or



from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        q = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        
        ans = []
        
        while len(q) != 0:
            n = q.popleft()
            ans.append(n)
            for v in graph[n]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        for v in indegree:
            if v != 0:
                return []
        
        return ans
