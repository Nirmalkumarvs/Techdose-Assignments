class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        if not root: 
            return [] 
        hashMap = defaultdict(list) 
        def dfs(root,row=0): 
            if not root: 
                return None  
            
            hashMap[row].append(root.val)
            dfs(root.left, row+1) 
            dfs(root.right, row+1) 
            
        dfs(root,0)
        return [hashMap[x] for x in hashMap]
        
