#Bellman ford algorithm:
def bellman(nodes,graph,src):
    path_len={v:float('inf') for v in nodes}
    path_lengths[src]=0
    for i in range(len(nodes)-1):
        for s,d,p in graph:
            if path_len[s] + p < path_len[d]:
                path_len[d]=path_len[s]+p
    return path_len
