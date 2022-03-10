class Solution:
    # dijktras
    def findCheapestPrice(n, flights, src, dst, K):
	graph = collections.defaultdict(dict)
	for s, d, w in flights:
		graph[s][d] = w
	pq = [(0, src, K+1)]
	vis = [0] * n
	while pq:
		w, x, k = heapq.heappop(pq)
		if x == dst:
			return w
		if vis[x] >= k:
			continue
		vis[x] = k
		for y, dw in graph[x].items():
			heapq.heappush(pq, (w+dw, y, k-1))
	return -1

    #Bellman ford 
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int: 
        prices=[float("inf")]*n  
        prices[src] = 0 
        
        for i in range(k+1): 
            temp = prices[::]
            for s,d,p in flights: 
                if prices[s] == float("inf"):  
                    continue 
                temp[d] = min(temp[d], prices[s] + p)
                
            prices=temp[::] 
        return -1 if prices[dst] == float("inf") else prices[dst]
                    
        
