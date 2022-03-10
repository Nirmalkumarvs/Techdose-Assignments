import heapq as hq
class Solution:
	def minimumEffortPath(self, heights: List[List[int]]) -> int:
		n = len(heights)
		m = len(heights[0])

		graph = defaultdict(list)
		op = [(0,-1),(0,1),(-1,0),(1,0)]
		 
		for i in range(n):
			for j in range(m):
				for r,c in op:
					row = i+r 
					col = j +c
					if 0 <= row < n and 0 <= col < m:
						graph[(i,j)].append((row,col))
		
		Q = [(0,(0,0))]
		visited = set()
		while Q:
			cost, vertex = hq.heappop(Q)
			r,c = vertex
			if vertex == (n-1,m-1):
				return cost
			if vertex in visited:
				continue
			visited.add(vertex)
			for neib in graph[vertex]:
				nr, nc = neib
				new_cost = max(abs(heights[r][c]-heights[nr][nc]), cost)
				hq.heappush(Q, (new_cost, neib) )
