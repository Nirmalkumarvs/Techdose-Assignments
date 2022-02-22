class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root, mini, maxi):
            if not root: return True
            
            if not(mini < root.val < maxi):
                return False
            
            return rec(root.left, mini, root.val) and rec(root.right,root.val,maxi)
        
        return rec(root, -inf, inf)
