class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]: 
        hashMap=defaultdict(lambda : defaultdict(list))  
        q=[[root,0,0]]  
        mini=inf 
        maxi=-inf
        while q: 
            node, col, row = q.pop(0) 
            hashMap[col][row].append(node.val)
            
            mini = min(mini, col) 
            maxi = max(maxi, col) 
            if node.left: 
                q.append([node.left,col-1,row+1])
            if node.right: 
                q.append([node.right,col+1,row+1])
        ms=[]
        for x in range(mini,maxi+1): 
            rs=[]
            for i in hashMap[x].values(): 
                rs+=sorted(i) 
            ms.append(rs[::])
        return ms
        
