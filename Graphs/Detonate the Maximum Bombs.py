class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        cnt,n=0,len(bombs)
        ori=set(range(n))
        dic={}
        for i in range(n):
            dic[i]=set()
    
        for i in range(n):
            [x1,y1,r1]=bombs[i]
            for j in range(i+1,n):
                [x2,y2,r2]=bombs[j]
            
                sqare_distance=pow(x1-x2,2)+pow(y1-y2,2)                
                if sqare_distance<=pow(r1,2):
                    dic[i].add(j)
                if sqare_distance<=pow(r2,2):
                    dic[j].add(i)
            
        while ori:
            i=ori.pop()
            cur=diff=dic[i]          
            cur.add(i)
            pre=cur           
                    
            while diff:                
                for next in diff:
                    cur=cur|dic[next]                    
            
                diff=cur-pre
                pre=cur              
        
            ori-=pre                                  
            cnt=max(cnt,len(cur))
            
        return cnt
        
