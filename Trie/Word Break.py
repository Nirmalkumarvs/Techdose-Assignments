class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.flag = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur.children: return False
            cur = cur.children[c]
        return cur.flag

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        trie = Trie()
        
        for w in wordDict:
            trie.insert(w)
        
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        
        for i in range(1,len(s)+1):
            for j in range(i):
                
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True 
                    
                    
            
        return dp[-1]
