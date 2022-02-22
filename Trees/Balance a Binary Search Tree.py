class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(root, res): 
            if root: 
                inorder(root.left, res)  
                res.append(root)
                inorder(root.right, res)
        
        def construct(res, left, right): 
            if left > right: 
                return None
            mid = (left + right) // 2 
            node = res[mid] 
            node.left = construct(res, left, mid-1)
            node.right = construct(res, mid+1, right) 
            return node   
        
        res=[]
        inorder(root,res)
        return construct(res, 0, len(res)-1)
