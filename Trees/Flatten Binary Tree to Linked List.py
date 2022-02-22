class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None: 
        curr = root 
        while curr:
            if curr.left: 
                pre = nxt = curr.left 
                
                while pre.right: 
                    pre = pre.right 
                    
                pre.right = curr.right 
                curr.left = None 
                curr.right = nxt  
                
            curr = curr.right
            
        return root
