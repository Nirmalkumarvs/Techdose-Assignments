class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = [float('inf')] * N
        dist[K-1] = 0
        seen = set()
        while pq:
            d, node = heapq.heappop(pq)
            if node in seen: 
                continue
            
            seen.add(node)
            for nei, d2 in graph[node]:
                if nei not in seen:
                    if d+d2 < dist[nei-1]:
                        heapq.heappush(pq, (d+d2, nei))
                        dist[nei-1] = d+d2

        return max(dist) if sum(dist) < float('inf') else -1
