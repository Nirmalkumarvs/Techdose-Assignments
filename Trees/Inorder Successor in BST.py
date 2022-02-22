class Solution:
    
    def inorderSuccessor(self, root, p):
        if root == None:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        
        left = self.inorderSuccessor(root.left, p)
        
        if left != None:
            return left
        else:
            return root
