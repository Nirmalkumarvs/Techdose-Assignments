class TrieNode:
     
    def __init__(self):
    
        self.children = dict()
        self.isEndOfWord = False
        self.num = dict()
 

root = None
 

def getNewTrieNode():
     
    pNode = TrieNode()
    return pNode
  

def insertWord(word):
     
    global root
     
    current = root
  
    s = ''
  
    for i in range(len(word)):
        s = word[i]
        
        if (s not in current.children):
            p = getNewTrieNode()
            current.children[s] = p
            current.num[s] = 1
        else:
            current.num[s] = current.num[s] + 1
  
        current = current.children[s]
     
    current.isEndOfWord = True
 

def countWords(words, prefix):
     
    global root
    root = getNewTrieNode()
  
    n = len(words)
  
    for i in range(n):
        insertWord(words[i])
         
    current = root
    s = ''
  
    wordCount = 0
     
    for i in range(len(prefix)):
        s = prefix[i]

        if (s not in current.children):
            wordCount = 0
            break
         
        wordCount = (current.num)[s]
  
        current = (current.children)[s]
  
    return wordCount
 


     
words = [ "apk", "app", "apple","arp", "array" ]
  
prefix = "ap"
  
print(countWords(words, prefix))
     
