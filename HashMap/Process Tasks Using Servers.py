class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        servers = [(w, j) for j, w in enumerate(servers)]
        heapq.heapify(servers)
        exe = []  
        
        t=0
        m=len(tasks)
        res=[0]*m 
        
        for i in range(len(tasks)):    
            t=max(t,i) 
            
            if servers==[]:
                t=exe[0][0]
            while exe and t>=exe[0][0]: 
                timefree, weight, index = heapq.heappop(exe) 
                heapq.heappush(servers,(weight,index)) 
                
            weight, index = heapq.heappop(servers) 
            res[i]=index 
            heapq.heappush(exe,(t+tasks[i],weight,index))  
            
        return res
        
