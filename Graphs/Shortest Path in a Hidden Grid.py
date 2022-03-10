def maximumMinimumPath(self, a: List[List[int]]) -> int:
        import heapq
        rl = len(a)
        cl = len(a[0])
        rrange = range(rl)
        crange = range(cl)
        heap = [(-a[0][0], 0, 0)]  # - val, row, col
        visited = {(0, 0)}
        neighbours = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while heap:
            val, row, col = heapq.heappop(heap)
            if row == rl - 1 and col == cl - 1:
                return - val
            for nrow, ncol in neighbours:
                nrow += row
                ncol += col
                if nrow in rrange and ncol in crange and (nrow, ncol) not in visited:
                    visited.add((nrow, ncol))
                    heapq.heappush(heap, (max(-a[nrow][ncol], val), nrow, ncol))
        return -1
