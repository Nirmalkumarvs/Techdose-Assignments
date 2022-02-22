class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
    
        def getBoxID(row,col):
            colVal,rowVal=math.floor(col/3),math.floor(row/3)*3
            return colVal+rowVal
        
        
        def isValid(box,row,col,num):
            if num in box or num in row or num in col:
                return False
            else:
                return True
        
        def solveBacktrack(board,boxes,rows,cols,r,c):
           
            if r==len(board) or c==len(board[0]):
                return True
            else:
                if board[r][c]=='.':
                    for num in range(1,10):
                        str_num=str(num)
                        
                        
                        board[r][c]=str_num
                        boxID=getBoxID(r,c)
                        box=boxes[boxID]
                        row=rows[r]
                        col=cols[c] 
                        
                        if isValid(box,row,col,str_num): 
                            
                            boxes[boxID][str_num]=True 
                            rows[r][str_num]=True
                            cols[c][str_num]=True
                            
                            
                            if c==len(board[0])-1: 
                                if solveBacktrack(board,boxes,rows,cols,r+1,0):
                                    return True
                            else: 
                                if solveBacktrack(board,boxes,rows,cols,r,c+1):
                                    return True
                                
                            # Undo
                            del boxes[boxID][str_num]
                            del rows[r][str_num]
                            del cols[c][str_num]
                        board[r][c]='.'
                else:
                    if c==len(board[0])-1: 
                        if solveBacktrack(board,boxes,rows,cols,r+1,0):
                            return True
                    else:
                        if solveBacktrack(board,boxes,rows,cols,r,c+1):       
                            return True
                    
                    
                    
        
        n=len(board)
        boxes=[{} for _ in range(n)]
        rows=[{} for _ in range(n)] 
        cols=[{} for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                if board[r][c]!='.':
                    val=board[r][c]
                    boxID=getBoxID(r,c)
                    boxes[boxID][val]=True
                    rows[r][val]=True
                    cols[c][val]=True
        
        
        solveBacktrack(board,boxes,rows,cols,0,0)
        return board
