class Solution:
    
    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node)
        self.inorder(node.right, res)

    
    
    def treeToDoublyList(self, root):
        
        if not root:
            return root
        
        first = None
        last = None
        prev = None

        res = []
        self.inorder(root,res)
	
        for v in res:
            if first is None:
                first = v
            last = v
            if prev is not None:
                prev.right = v
                v.left = prev
            prev = v
            
        first.left = last
        last.right = first
        return first
