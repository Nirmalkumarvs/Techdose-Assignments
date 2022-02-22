class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            result.append(queue[-1].val)
            
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        
        return result
