class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * n for _ in range(n)]
        for i, j in prerequisites:
            reachable[i][j] = True

        for node in range(n):
            for i in range(n):
                for j in range(n):
                    reachable[i][j] = reachable[i][j] or (reachable[i][node] and reachable[node][j])
        
        result=[]
        for element in queries:
            result.append(reachable[element[0]][element[1]])
        return result
