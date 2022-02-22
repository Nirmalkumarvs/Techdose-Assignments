class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.search(root, root.val)
    
    def search(self, node, previous):
        if node == None:
            return 0
        elif previous <= node.val:
            return 1 + self.search(node.left, node.val) + self.search(node.right, node.val)
        else:
            return self.search(node.left, previous) + self.search(node.right, previous)
