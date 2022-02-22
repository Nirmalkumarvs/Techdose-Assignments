class Solution:
        

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        if root is None:
            return root
        
        if root in [p, q]:
            return root
        
        left_res = self.lowestCommonAncestor(root.left, p, q)
        
        right_res = self.lowestCommonAncestor(root.right, p, q)
        
        if left_res and right_res:
            return root
        
        return left_res or right_res 
           
