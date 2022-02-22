class TrieNode:
    
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.node
        
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr=curr.child[char]
        
        curr.end=True
    
    def dfs(self,index,word,node):
        if index>=self.wordlen: 
            return node.end 
        
        curr = word[index] 
        
        if curr==".": 
            if len(node.child) == 0: 
                return False 
            else: 
                for i in node.child: 
                    if self.dfs(index+1,word,node.child[i]):
                        return True 
        else: 
            if curr not in node.child: 
                return False 
            else: 
                return self.dfs(index+1,word,node.child[curr])
        
    
    def search(self, word: str) -> bool: 
        self.wordlen = len(word)
        return self.dfs(0,word,self.node)
