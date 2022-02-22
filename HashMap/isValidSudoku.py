def isValidSudoku(self, board):
        hashMap = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                val = board[i][j]
                if val != ".":
                    ssIndex = (i//3)*3+(j//3)
                    if not val in hashMap:
                        hashMap[val] = [(i, j, ssIndex)]
                    else:
                        for ii in hashMap[val]:
                            if i == ii[0] or j == ii[1] or ssIndex == ii[2]:
                                return False
                        hashMap[val].append((i, j, ssIndex))
                        
        
        return True  
