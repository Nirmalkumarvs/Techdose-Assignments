class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        g = defaultdict(list)
        get_dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        for i in range(n):
            for j in range(i + 1, n):
                dist = get_dist(points[i], points[j])
                g[i].append((dist, j))
                g[j].append((dist, i))
        costs = 0
        visited = set()
        q = [(0, 0)]
        while len(visited) < n:
            cost, index = heappop(q)
            if index not in visited:
                costs += cost
                visited.add(index)
                for edge_cost, next_index in g[index]:
                    heappush(q, (edge_cost, next_index))
        return costs
