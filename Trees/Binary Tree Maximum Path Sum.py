class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        
        def dfs(root): 
            if not root: 
                return 0 
            
            l = dfs(root.left) 
            r = dfs(root.right) 
            l = max(l,0) 
            r = max(r,0) 
            
            res[0]=max(res[0], root.val+l+r) 
            
            return root.val + max(l,r) 
        
        dfs(root) 
        return res[0]
