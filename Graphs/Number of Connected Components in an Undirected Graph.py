class solution:
    def countComponents(self,n,edges):
        par = [i for i in range(n)]
        rank = [1]*n
        def find(n1):
            res = n1
            while res != par[res]:
                par[res]=par[par[res]]
                res = par[res]
            return res
        def union(a,b):
            par_a, par_b = find(a), find(b)
            if par_a == par_b:
                return 0
            if rank[par_b] > rank[par_a]:
                par[par_a] = par_b
                rank[par_b] += rank[par_a]
            else:
                par[par_b] = par_a
                rank[par_a] += rank[par_b]
            return 1
        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res 
