class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return -1
            
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            
            res[0] = max(res[0],left+right)
            return max(left,right) 
        
        dfs(root)
        return res[0]
