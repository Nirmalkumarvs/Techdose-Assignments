class Solution:
    
    def colArea(self, li):
        max_area = 0
        for i in range(len(li)):
            temp = 1
            for j in range(i-1,-1,-1):
                if li[j] < li[i]:
                    break
                else:
                    temp+=1
            for j in range(i+1,len(li)):
                if li[j] < li[i]:
                    break
                else:
                    temp+=1
            temp = temp*li[i]
            max_area = max(max_area,temp)
        return max_area
    
    def maximalRectangle(self, matrix):
        if matrix == []:
            return 0
        
        R = len(matrix)
        C = len(matrix[0])
        
        max_area = 0
        
        for i in range(R):
            for j in range(C):
                matrix[i][j] = int(matrix[i][j])
        
        for i in range(R):
            for j in range(C):
                if i != 0 and matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        
        for li in matrix:
            max_area = max(max_area,self.colArea(li))
            
        return max_area
