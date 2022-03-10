class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance_matrix = []
        max_dist = 1e15
        for i in range(n):
            distance_matrix.append([max_dist for i in range(n)])
            distance_matrix[-1][i] = 0
        
        for i_city, j_city, distance in edges:
            distance_matrix[i_city][j_city] = distance
            distance_matrix[j_city][i_city] = distance
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    shortcut = distance_matrix[i][k] + distance_matrix[k][j]
                    if shortcut < distance_matrix[i][j]:
                        distance_matrix[i][j] = shortcut
        
        min_cities, return_idx = n + 1, -1
        print(distance_matrix)
        for i_city in range(n):
            close_cities = sum([dist <= distanceThreshold for dist in distance_matrix[i_city]])
            if close_cities <= min_cities:
                return_idx = i_city
                min_cities = close_cities
        return return_idx
