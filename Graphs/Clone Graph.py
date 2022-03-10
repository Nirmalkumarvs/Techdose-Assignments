class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashMap= {}
        
        def dfs(node):
            if node in hashMap:
                return hashMap[node]
            copy = Node(node.val)            
            hashMap[node] = copy
            
            
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        return dfs(node) if node else None
