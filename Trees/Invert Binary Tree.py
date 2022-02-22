class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        def invert(root):
            if not root:
                return;
            left_temp = root.left;
            root.left = root.right;
            root.right = left_temp;
            
            invert(root.left);
            invert(root.right);
            return root;
        
        return invert(root);
        
