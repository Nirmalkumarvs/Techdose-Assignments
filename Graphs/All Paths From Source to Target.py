class Solution:
    def dfs(self, curr, graph, path, paths, N):
        if curr == N-1:
            paths.append(path)
        else:
            for neighbor in graph[curr]:
                self.dfs(neighbor, graph, path + [neighbor], paths, N)
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        paths = []
        self.dfs(0, graph, [0], paths, N)
        return paths
