class TrieNode:
    
    def __init__(self):
        self.edges=dict()
        self.end=False
    
    def add(self,word):
        node=self
        for char in word:
            if char not in node.edges:
                 node.edges[char]=TrieNode()
            node=node.edges[char]
        node.end=True
    
    def search(self,word):
        node=self
        for char in word:
            if char not in node.edges:
                return False
            else:
                node=node.edges[char]
        return node.end

class Solution:
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        
        strs=[bin(num)[2:] for num in nums]
        N=max(((len(string) for string in strs)))
        strs=['0'*(N-len(string))+string for string in strs]
        
    
        trie=TrieNode()
        for string in strs:
            trie.add(string)
            
        output=0
        for string in strs:
            max_xor_string=''
            node=trie
            for i,char in enumerate(string):
                complement='0' if char=='1' else '1'
                if complement in node.edges:
                    node=node.edges[complement]
                    max_xor_string+=complement
                else:
                    node=node.edges[char]
                    max_xor_string+=char 
                    
            max_xor=int(max_xor_string, base=2)^int(string,base=2)
            output=max(output,max_xor)
        
        return output
