class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 
        def check(left, right):  
            
            if left == None and right != None or left != None and right == None:  
                return False
            
            if left == None and right == None: 
                return True
    
            if left.val!=right.val: 
                return False
            
            return check(left.right, right.left) and check(left.left, right.right) 
        
        return check(root.left, root.right)
        
