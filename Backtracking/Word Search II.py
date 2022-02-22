class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_word_end = False
        self.word = ''
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            cur = trie
            for c in word:
                cur = cur.children[c]
            cur.is_word_end = True
            cur.word = word
                    
        def backtrack(x,y,cur):
            if cur.is_word_end:
                res.append(cur.word)
                cur.is_word_end = False
            
            for dx,dy in neighbors:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx,ny) not in seen and board[nx][ny] in cur.children:
                    seen.add((nx,ny))
                    backtrack(nx,ny,cur.children[board[nx][ny]])
                    seen.remove((nx,ny))
        res = []
        n = len(board)
        m = len(board[0])
        neighbors = [(1,0),(-1,0),(0,-1),(0,1)]
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie.children:
                    seen = set([(i,j)])
                    backtrack(i,j,trie.children[board[i][j]])
        
        return res
