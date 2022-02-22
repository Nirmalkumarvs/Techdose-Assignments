class Trie:

    def __init__(self): 
        self.child = defaultdict(Trie) 
        self.end = False

    def insert(self, word: str) -> None:
        if word: 
            ch = word[0] 
            if len(word)==1: 
                self.child[ch].end = True 
            else: 
                self.child[ch].insert(word[1:])
            
    def search(self, word: str, isprefixsearch=False ) -> bool:
        if word: 
            ch = word[0] 
            if len(word)==1 and ch in self.child: 
                return self.child[ch].end or isprefixsearch 
            
            if ch in self.child: 
                return self.child[ch].search(word[1:],isprefixsearch) 
            else: 
                return False
                

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)

or

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

    def startsWith(self, prefix: str) -> bool:
        cur= self.root
        for c in prefix:
            if not c in cur.children: return False
            cur= cur.children[c]
        return True
    
