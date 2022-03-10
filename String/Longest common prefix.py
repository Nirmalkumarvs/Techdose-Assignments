class Trienode:
    def __init__(self):
        self.child = dict()
        self.end = False

def search(root,s):
    temp=root
    for i in s:
        if i not in temp.child:
            return False
        temp=temp.child[i] 
    return temp.end

def longestPre(roott):
        root = roott
        res = ''
        while root:
            if len(root.child) > 1 or root.end:
                return res
            
            key = list(root.child)[0]
            res += key
            
            root = root.child[key]
        return res
        
a=["tree","treach","trunck","trrun"]
root=Trienode()
for i in a:
    temp=root
    for j in i:
        if j not in temp.child:
            temp.child[j]=Trienode()
        temp=temp.child[j]
    temp.end=True

print(search(root,"tree"))
print(longestPre(root))
