class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]: 
        if not preorder: 
            return None 
        node = TreeNode(preorder[0]) 
        j = 1 
        while j<len(preorder) and preorder[j]<preorder[0]: 
            j+=1  
        node.left = self.bstFromPreorder(preorder[1:j])
        node.right = self.bstFromPreorder(preorder[j:]) 
        return node
or


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def bisectLeft(target, lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if preorder[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1 
            return lo
            
        def recurBuild(lo, hi):
            if lo > hi:
                return None
            
            nodeVal = preorder[lo]
            node = TreeNode(nodeVal)
            
            mid = bisectLeft(nodeVal, lo + 1, hi)
            
            node.left = recurBuild(lo + 1, mid - 1)
            node.right = recurBuild(mid, hi)
            
            return node
    
        return recurBuild(0, len(preorder) - 1)
            
            
