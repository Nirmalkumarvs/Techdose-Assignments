from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:    
        
        # matrix is n x n
        n = len(matrix)
        
        # heap
        h = []
        # used to track advancement per row
        indices = [0 for i in range(n)]
        # we insert the first element from each row into the heap, 
        # the indices array serves to know which col to push into the heap per row
        for row in range(n):
            heappush(h, (matrix[row][0], row))
        
        # We remove k-1 elements, so the remaining kth element will be the minimum of the remaining heap
        i = 0
        while i < k-1:
            value, row = heappop(h)
            
            # We add the next number from the popped row, if any is left
            col = indices[row]
            if col < cols-1: 
                indices[row] += 1
                heappush(h, (matrix[row][col+1], row))
            i += 1
        
        return h[0][0]
