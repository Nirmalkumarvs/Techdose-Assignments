from collections import deque,defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]: 
        parents={}  
        
        def dfs(node,par=None): 
            if not node: 
                return None  
            parents[node]=par 
            dfs(node.left,node) 
            dfs(node.right,node) 
            
        dfs(root,None)    
        q=deque() 
        q.append([target,0]) 
        vis = defaultdict(lambda:False) 
        res=[] 
        level = 0 
        while q:  
            node, level = q.popleft() 
            if not vis[node]:
                if level==k: 
                    res.append(node.val) 
                vis[node]=True
                if node.left is not None and not vis[node.left]:
                    q.append((node.left,level+1))
                if node.right is not None and not vis[node.right]:
                    q.append((node.right,level+1))
                par=parents[node]
                if par is not None and not vis[par]:
                    q.append((par,level+1))
        return res
                
                
            
        
