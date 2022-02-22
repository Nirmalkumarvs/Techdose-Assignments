class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  
        c = 0
        d=defaultdict(list)
        def dfs(root,c):
            if root is not None:
                d[c].append(root.val)
            
                dfs(root.left,c+1)
                dfs(root.right,c+1)

        dfs(root,c)
        res, p = [], 1
        for i in d:
            res.append(d[i][::p]) 
            p=p*-1
        return res
                
