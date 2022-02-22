class Solution(object):
    def verticalTraversal(self, root): 
        d={}
        def traverse(root,val,h): 
            if root==None: 
                return  
            if val in d: 
                d[val].append([root.val,val,h]) 
            else: 
                d[val]=[[root.val,val,h]]  
            traverse(root.left,val-1,h+1) 
            traverse(root.right,val+1,h+1) 
        
        traverse(root,0,0)  
        print(d)
        d=[i[1] for i in sorted(d.items(),key=lambda x:x[0])]  
        m=[]
        for i in d:  
            print(i)
            k=[j[0] for j in sorted(i,key=lambda x:(x[-1],x[0]))]  
            print(k)
           
            m.append(k)
        return m
            
