class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        startRow,endRow=0,len(matrix)-1
        startCol,endCol=0,len(matrix[0])-1
        
        while startRow<=endRow and startCol<=endCol:
            
            for i in range(startCol,endCol+1):
                result.append(matrix[startRow][i])
           
            for i in range(startRow+1,endRow+1):
                result.append(matrix[i][endCol]) 
            
            for i in reversed(range(startCol,endCol)):
                if startRow==endRow:
                    break
                result.append(matrix[endRow][i])
            for i in reversed(range(startRow+1,endRow)):
                if startCol==endCol:
                    break
                result.append(matrix[i][startCol])
            startRow+=1
            endRow-=1
            startCol+=1
            endCol-=1
        return result
            
