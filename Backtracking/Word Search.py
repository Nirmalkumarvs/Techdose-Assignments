class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:

        board_count = Counter(char for rows in board for char in rows) 
        
        
        for word_char, need in Counter(word).items():
            if need > board_count[word_char]: 
                return False

        m = len(board)
        n = len(board[0])

        def backtracking(x, y, index):
            if board[x][y] != word[index]: 
                return False
            
            if index == len(word) - 1: 
                return True
            
            pre = board[x][y]
            board[x][y] = ""
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if backtracking(nx, ny, index + 1): 
                        return True

            board[x][y] = pre
            return False

        return any(backtracking(x, y, 0) for x in range(m) for y in range(n))
                        
                        
                        
        return False
